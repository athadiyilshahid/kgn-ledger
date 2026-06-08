from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db
from app import models

router = APIRouter(prefix="/purchases", tags=["Purchases"])


# ➤ CREATE PURCHASE (with GST calculation)
@router.post("/")
def create_purchase(
    supplier_name: str,
    gstin: str = None,
    invoice_number: str = None,
    taxable_amount: float = 0,
    gst_rate: float = 0,
    db: Session = Depends(get_db)
):
    gst_amount = (taxable_amount * gst_rate) / 100
    total_amount = taxable_amount + gst_amount

    purchase = models.Purchase(
        supplier_name=supplier_name,
        gstin=gstin,
        invoice_number=invoice_number,
        taxable_amount=taxable_amount,
        gst_rate=gst_rate,
        gst_amount=gst_amount,
        total_amount=total_amount
    )

    db.add(purchase)
    db.commit()
    db.refresh(purchase)

    return {
        "message": "Purchase created successfully",
        "data": purchase
    }


# ➤ GET ALL PURCHASES
@router.get("/")
def get_purchases(db: Session = Depends(get_db)):
    return db.query(models.Purchase).all()


# ➤ GET SINGLE PURCHASE
@router.get("/{purchase_id}")
def get_purchase(purchase_id: int, db: Session = Depends(get_db)):
    purchase = db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()

    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")

    return purchase


# ➤ DELETE PURCHASE
@router.delete("/{purchase_id}")
def delete_purchase(purchase_id: int, db: Session = Depends(get_db)):
    purchase = db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()

    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")

    db.delete(purchase)
    db.commit()

    return {"message": "Purchase deleted successfully"}