from sqlalchemy.orm import Session
from app import models, schemas


# =====================================================
# 👤 USERS (BASIC CRUD - OPTIONAL FOR AUTH SYSTEM)
# =====================================================

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        password_hash=hashed_password,
        role="staff"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# =====================================================
# 🧾 SALES CRUD
# =====================================================

def create_sale(db: Session, sale: schemas.SaleCreate):
    db_sale = models.Sale(
        customer_name=sale.customer_name,
        gstin=sale.gstin,
        invoice_number=sale.invoice_number,
        taxable_amount=sale.taxable_amount,
        gst_rate=sale.gst_rate,
        gst_amount=sale.gst_amount,
        total_amount=sale.total_amount,
        sale_date=sale.sale_date
    )

    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale


def get_sales(db: Session):
    return db.query(models.Sale).all()


def get_sale(db: Session, sale_id: int):
    return db.query(models.Sale).filter(models.Sale.id == sale_id).first()


def delete_sale(db: Session, sale_id: int):
    sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if sale:
        db.delete(sale)
        db.commit()
    return sale


# =====================================================
# 🛒 PURCHASES CRUD
# =====================================================

def create_purchase(db: Session, purchase: schemas.PurchaseCreate):
    db_purchase = models.Purchase(
        supplier_name=purchase.supplier_name,
        gstin=purchase.gstin,
        invoice_number=purchase.invoice_number,
        taxable_amount=purchase.taxable_amount,
        gst_rate=purchase.gst_rate,
        gst_amount=purchase.gst_amount,
        total_amount=purchase.total_amount,
        purchase_date=purchase.purchase_date
    )

    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase


def get_purchases(db: Session):
    return db.query(models.Purchase).all()


def get_purchase(db: Session, purchase_id: int):
    return db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()


# =====================================================
# 💰 EXPENSES CRUD
# =====================================================

def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(
        category=expense.category,
        amount=expense.amount,
        remarks=expense.remarks,
        expense_date=expense.expense_date
    )

    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


def get_expenses(db: Session):
    return db.query(models.Expense).all()


# =====================================================
# 📒 LEDGER CRUD
# =====================================================

def create_ledger_entry(db: Session, ledger: schemas.LedgerCreate):
    db_entry = models.LedgerEntry(
        partner_id=ledger.partner_id,
        description=ledger.description,
        debit=ledger.debit,
        credit=ledger.credit,
        reference_type=ledger.reference_type,
        reference_id=ledger.reference_id,
        created_by=ledger.created_by
    )

    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def get_ledger_entries(db: Session):
    return db.query(models.LedgerEntry).all()