from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.core.security import verify_token
from app import models

# Login endpoint
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)


# =========================
# DATABASE SESSION
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# CURRENT USER
# =========================
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # verify JWT token
    token_data = verify_token(token)

    if token_data is None:
        raise credentials_exception

    # support both verify_token returning dict or user_id
    if isinstance(token_data, dict):
        user_id = token_data.get("user_id")
    else:
        user_id = token_data

    if user_id is None:
        raise credentials_exception

    # find user in database
    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if user is None:
        raise credentials_exception

    return user