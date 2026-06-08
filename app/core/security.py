from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# =========================
# 🔐 CONFIG
# =========================

SECRET_KEY = "kgn-ledger-super-secure-2026-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 day

# =========================
# 🔑 PASSWORD HASHING
# =========================

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash plain password before storing in DB
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify login password against stored hash
    """
    return pwd_context.verify(plain_password, hashed_password)


# =========================
# 🔐 JWT TOKEN
# =========================

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Create JWT access token
    """
    to_encode = data.copy()

    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


# =========================
# 🔍 DECODE TOKEN (OPTIONAL BUT USEFUL)
# =========================

def decode_access_token(token: str):
    """
    Decode JWT token and return payload
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None