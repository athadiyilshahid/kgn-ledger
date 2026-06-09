from fastapi import FastAPI

from app.database import Base, engine
from app import models

from app.routers import (
    users,
    sales,
    purchases,
    expenses,
    ledger
)

app = FastAPI(title="KGN Ledger API")


# =========================
# CREATE TABLES ON STARTUP
# =========================
@app.on_event("startup")
def startup():
    # This ensures all tables exist in PostgreSQL (Render/Neon)
    Base.metadata.create_all(bind=engine)


# =========================
# ROUTERS
# =========================
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(sales.router, prefix="/sales", tags=["Sales"])
app.include_router(purchases.router, prefix="/purchases", tags=["Purchases"])
app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])
app.include_router(ledger.router, prefix="/ledger", tags=["Ledger"])


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def root():
    return {
        "message": "KGN Ledger API is running"
    }