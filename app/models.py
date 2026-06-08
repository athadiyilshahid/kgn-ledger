from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


# -------------------------
# USERS
# -------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


# -------------------------
# SALES
# -------------------------
class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    gst_amount = Column(Float, default=0.0)
    total_amount = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


# -------------------------
# PURCHASES
# -------------------------
class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    supplier_name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    gst_amount = Column(Float, default=0.0)
    total_amount = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


# -------------------------
# EXPENSES
# -------------------------
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


# -------------------------
# LEDGER
# -------------------------
class LedgerEntry(Base):
    __tablename__ = "ledger_entries"

    id = Column(Integer, primary_key=True, index=True)

    entry_type = Column(String, nullable=False)  
    # "SALE", "PURCHASE", "EXPENSE"

    reference_id = Column(Integer, nullable=False)

    debit = Column(Float, default=0.0)
    credit = Column(Float, default=0.0)

    description = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())