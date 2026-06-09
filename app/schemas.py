from pydantic import BaseModel, EmailStr, ConfigDict


# =========================
# USER SCHEMAS
# =========================

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
    is_active: bool

    # Pydantic v2 way (IMPORTANT FIX)
    model_config = ConfigDict(from_attributes=True)


# =========================
# TOKEN SCHEMAS
# =========================

class Token(BaseModel):
    access_token: str
    token_type: str


# =========================
# SALES SCHEMAS
# =========================

class SaleCreate(BaseModel):
    item: str
    quantity: int
    price: float


class SaleResponse(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    total: float

    model_config = ConfigDict(from_attributes=True)


# =========================
# PURCHASE SCHEMAS
# =========================

class PurchaseCreate(BaseModel):
    item: str
    quantity: int
    cost: float


class PurchaseResponse(BaseModel):
    id: int
    item: str
    quantity: int
    cost: float
    total: float

    model_config = ConfigDict(from_attributes=True)


# =========================
# EXPENSE SCHEMAS
# =========================

class ExpenseCreate(BaseModel):
    description: str
    amount: float


class ExpenseResponse(BaseModel):
    id: int
    description: str
    amount: float

    model_config = ConfigDict(from_attributes=True)


# =========================
# LEDGER SCHEMAS
# =========================

class LedgerEntryCreate(BaseModel):
    description: str
    debit: float = 0
    credit: float = 0


class LedgerEntryResponse(BaseModel):
    id: int
    description: str
    debit: float
    credit: float

    model_config = ConfigDict(from_attributes=True)