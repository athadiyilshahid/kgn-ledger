from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.deps import get_db, get_current_user
from app.models import User

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


# =========================
# CREATE SALE
# =========================
@router.post(
    "/",
    response_model=schemas.SaleResponse,
    status_code=status.HTTP_201_CREATED
)
def create_sale(
    sale: schemas.SaleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return crud.create_sale(db=db, sale=sale)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error creating sale: {str(e)}"
        )


# =========================
# GET ALL SALES
# =========================
@router.get(
    "/",
    response_model=List[schemas.SaleResponse]
)
def get_sales(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_sales(db)


# =========================
# GET SINGLE SALE
# =========================
@router.get(
    "/{sale_id}",
    response_model=schemas.SaleResponse
)
def get_sale(
    sale_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    sale = crud.get_sale(db, sale_id)

    if not sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale not found"
        )

    return sale


# =========================
# DELETE SALE
# =========================
@router.delete(
    "/{sale_id}",
    status_code=status.HTTP_200_OK
)
def delete_sale(
    sale_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    sale = crud.delete_sale(db, sale_id)

    if not sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale not found"
        )

    return {
        "message": "Sale deleted successfully"
    }