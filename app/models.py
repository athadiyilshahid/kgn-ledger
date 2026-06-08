from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Numeric, ForeignKey
from sqlalchemy.sql import func

from app.database import Base


# =========================
# 👤 USERS
# =========================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(15))
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(String(20), default="staff")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# =========================
# 🤝 PARTNERS
# =========================

class Partner(Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(15))
    share_percentage = Column(Numeric(5, 2), default=0)
    capital_balance = Column(Numeric(12, 2), default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# =========================
# 📒 LEDGER
# =========================

class LedgerEntry(Base):
    __tablename__ = "ledger_entries"

    id = Column(Integer, primary_key=True, index=True)
    partner_id = Column(Integer, ForeignKey("partners.id"))
    entry_date = Column(Date, server_default=func.now())
    description = Column(Text)

    debit = Column(Numeric(12, 2), default=0)
    credit = Column(Numeric(12, 2), default=0)

    reference_type = Column(String(50))
    reference_id = Column(Integer)

    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# =========================
# 🛒 PURCHASES
# =========================

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    supplier_name = Column(String(100))
    gstin = Column(String(20))
    invoice_number = Column(String(50))

    taxable_amount = Column(Numeric(12, 2))
    gst_rate = Column(Numeric(5, 2))
    gst_amount = Column(Numeric(12, 2))
    total_amount = Column(Numeric(12, 2))

    purchase_date = Column(Date, server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# =========================
# 🧾 SALES
# =========================

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100))
    gstin = Column(String(20))
    invoice_number = Column(String(50))

    taxable_amount = Column(Numeric(12, 2))
    gst_rate = Column(Numeric(5, 2))
    gst_amount = Column(Numeric(12, 2))
    total_amount = Column(Numeric(12, 2))

    sale_date = Column(Date, server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# =========================
# 💰 EXPENSES
# =========================

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50))
    amount = Column(Numeric(12, 2))
    remarks = Column(Text)

    expense_date = Column(Date, server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# =========================
# 🧾 GST TRANSACTIONS
# =========================

class GSTTransaction(Base):
    __tablename__ = "gst_transactions"

    id = Column(Integer, primary_key=True, index=True)

    type = Column(String(20))  # INPUT / OUTPUT
    source_type = Column(String(20))  # purchase / sale
    source_id = Column(Integer)

    taxable_amount = Column(Numeric(12, 2))
    gst_rate = Column(Numeric(5, 2))

    cgst = Column(Numeric(12, 2), default=0)
    sgst = Column(Numeric(12, 2), default=0)
    igst = Column(Numeric(12, 2), default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())