from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import models
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


# =========================
# DATABASE DEPENDENCY
# =========================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# REGISTER USER
# =========================

@router.post("/register")
def register_user(
    name: str,
    email: str,
    password: str,
    phone: str | None = None,
    db: Session = Depends(get_db)
):

    # check if user exists
    existing_user = db.query(models.User).filter(models.User.email == email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # create new user
    new_user = models.User(
        name=name,
        email=email,
        phone=phone,
        password_hash=hash_password(password),
        role="staff"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


# =========================
# LOGIN USER
# =========================

@router.post("/login")
def login_user(
    email: str,
    password: str,
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(
        data={
            "user_id": user.id,
            "email": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }