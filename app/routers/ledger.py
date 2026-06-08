from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db
from app import models

router = APIRouter(prefix="/ledger", tags=["Ledger"])

# ➤ ADD LEDGER ENTRY
@router.post("/")
def add_ledger_entry(
    partner_id: int,
    description: str,
    debit: float = 0,
    credit: float = 0,
    db: Session = Depends(get_db)
):
    entry = models.LedgerEntry(
        partner_id=partner_id,
        description=description,
        debit=debit,
        credit=credit
    )

    db.add(entry)
    db.commit()
    db.refresh(entry)

    return {"message": "Ledger entry added", "data": entry}


# ➤ GET ALL LEDGER ENTRIES
@router.get("/")
def get_all_entries(db: Session = Depends(get_db)):
    return db.query(models.LedgerEntry).all()


# ➤ GET LEDGER BY PARTNER
@router.get("/{partner_id}")
def get_partner_ledger(partner_id: int, db: Session = Depends(get_db)):
    entries = db.query(models.LedgerEntry)\
        .filter(models.LedgerEntry.partner_id == partner_id)\
        .all()

    if not entries:
        raise HTTPException(status_code=404, detail="No ledger entries found")

    return entries


# ➤ DELETE LEDGER ENTRY
@router.delete("/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(models.LedgerEntry)\
        .filter(models.LedgerEntry.id == entry_id)\
        .first()

    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    db.delete(entry)
    db.commit()

    return {"message": "Ledger entry deleted"}