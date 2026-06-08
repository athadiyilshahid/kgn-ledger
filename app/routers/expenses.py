from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db
from app import models

router = APIRouter(prefix="/expenses", tags=["Expenses"])

# ➤ CREATE EXPENSE
@router.post("/")
def create_expense(
    category: str,
    amount: float,
    remarks: str = None,
    db: Session = Depends(get_db)
):
    expense = models.Expense(
        category=category,
        amount=amount,
        remarks=remarks
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)

    return {"message": "Expense added", "data": expense}


# ➤ GET ALL EXPENSES
@router.get("/")
def get_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()


# ➤ GET SINGLE EXPENSE
@router.get("/{expense_id}")
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense


# ➤ DELETE EXPENSE
@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted"}