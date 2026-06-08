from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.deps import get_db

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


# =========================
# ➕ CREATE SALE
# =========================
@router.post("/", response_model=schemas.SaleResponse)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_sale(db=db, sale=sale)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =========================
# 📄 GET ALL SALES
# =========================
@router.get("/", response_model=List[schemas.SaleResponse])
def get_sales(db: Session = Depends(get_db)):
    return crud.get_sales(db)


# =========================
# 🔍 GET SINGLE SALE
# =========================
@router.get("/{sale_id}", response_model=schemas.SaleResponse)
def get_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = crud.get_sale(db, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


# =========================
# ❌ DELETE SALE
# =========================
@router.delete("/{sale_id}")
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = crud.delete_sale(db, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")

    return {"message": "Sale deleted successfully"}