from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


# =========================
# 👤 USER SCHEMAS
# =========================

class UserCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# 🔐 AUTH SCHEMAS
# =========================

class Token(BaseModel):
    access_token: str
    token_type: str


class LoginRequest(BaseModel):
    email: str
    password: str


# =========================
# 🧾 SALES SCHEMAS
# =========================

class SaleCreate(BaseModel):
    customer_name: str
    gstin: Optional[str] = None
    invoice_number: str

    taxable_amount: float
    gst_rate: float
    gst_amount: float
    total_amount: float

    sale_date: Optional[date] = None


class SaleResponse(BaseModel):
    id: int
    customer_name: str
    gstin: Optional[str]
    invoice_number: str

    taxable_amount: float
    gst_rate: float
    gst_amount: float
    total_amount: float
    sale_date: date

    class Config:
        from_attributes = True


# =========================
# 🛒 PURCHASE SCHEMAS
# =========================

class PurchaseCreate(BaseModel):
    supplier_name: str
    gstin: Optional[str] = None
    invoice_number: str

    taxable_amount: float
    gst_rate: float
    gst_amount: float
    total_amount: float

    purchase_date: Optional[date] = None


class PurchaseResponse(BaseModel):
    id: int
    supplier_name: str
    gstin: Optional[str]
    invoice_number: str

    taxable_amount: float
    gst_rate: float
    gst_amount: float
    total_amount: float
    purchase_date: date

    class Config:
        from_attributes = True


# =========================
# 💰 EXPENSE SCHEMAS
# =========================

class ExpenseCreate(BaseModel):
    category: str
    amount: float
    remarks: Optional[str] = None
    expense_date: Optional[date] = None


class ExpenseResponse(BaseModel):
    id: int
    category: str
    amount: float
    remarks: Optional[str]
    expense_date: date

    class Config:
        from_attributes = True


# =========================
# 📒 LEDGER SCHEMAS
# =========================

class LedgerCreate(BaseModel):
    partner_id: int
    description: str

    debit: float = 0
    credit: float = 0

    reference_type: Optional[str] = None
    reference_id: Optional[int] = None

    created_by: Optional[int] = None


class LedgerResponse(BaseModel):
    id: int
    partner_id: int
    description: str

    debit: float
    credit: float

    reference_type: Optional[str]
    reference_id: Optional[int]

    created_by: Optional[int]
    entry_date: date

    class Config:
        from_attributes = True