from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db
from app import models
from app.core.security import hash_password

router = APIRouter(prefix="/users", tags=["Users"])


# ➤ CREATE USER (Admin use)
@router.post("/")
def create_user(
    name: str,
    email: str,
    phone: str = None,
    password: str = None,
    role: str = "staff",
    db: Session = Depends(get_db)
):
    # check if user exists
    existing_user = db.query(models.User).filter(models.User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = models.User(
        name=name,
        email=email,
        phone=phone,
        password_hash=hash_password(password),
        role=role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User created successfully", "user_id": user.id}


# ➤ GET ALL USERS
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


# ➤ GET SINGLE USER
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# ➤ DELETE USER
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}