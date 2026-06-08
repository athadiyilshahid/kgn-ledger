from pydantic import BaseModel, EmailStr
from typing import Optional


# ---------------- USER SCHEMAS ----------------

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool = True

    class Config:
        from_attributes = True


# ---------------- TOKEN SCHEMA ----------------

class Token(BaseModel):
    access_token: str
    token_type: str


# ---------------- SALES SCHEMAS ----------------

class SaleCreate(BaseModel):
    item: str
    quantity: int
    price: float


class SaleResponse(SaleCreate):
    id: int
    total: float

    class Config:
        from_attributes = True