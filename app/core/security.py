import hashlib
from passlib.context import CryptContext

# bcrypt context (force modern backend)
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# =========================
# FIX: bcrypt 72-byte limit
# =========================
def normalize_password(password: str) -> str:
    """
    bcrypt has a 72-byte limit.
    We safely pre-hash long passwords.
    """
    if len(password.encode("utf-8")) > 72:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
    return password


# =========================
# HASH PASSWORD
# =========================
def hash_password(password: str) -> str:
    password = normalize_password(password)
    return pwd_context.hash(password)


# =========================
# VERIFY PASSWORD
# =========================
def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password = normalize_password(plain_password)
    return pwd_context.verify(plain_password, hashed_password)