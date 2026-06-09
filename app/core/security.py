import os
from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

# =========================
# CONFIG
# =========================

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is missing in environment variables")


# =========================
# PASSWORD HASHING (ARGON2 ONLY)
# =========================

pwd_context = CryptContext(
    schemes=["argon2"],   # 🚀 NO bcrypt anywhere
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Hash password using Argon2 (secure + no 72-byte limit issue)
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password against stored hash
    """
    return pwd_context.verify(plain_password, hashed_password)


# =========================
# JWT TOKEN
# =========================

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("user_id")
    except Exception:
        return None