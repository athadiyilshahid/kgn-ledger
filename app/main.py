from fastapi import FastAPI

# Import DB + Base
from app.database import Base, engine

# IMPORTANT: ensures all models are registered
from app import models

# Routers
from app.routers import users, sales, purchases, expenses, ledger


# =========================
# APP INITIALIZATION
# =========================
app = FastAPI(
    title="KGN Ledger API",
    version="1.0.0"
)


# =========================
# CREATE TABLES ON STARTUP
# =========================
@app.on_event("startup")
def startup():
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
        "message": "KGN Ledger API is running",
        "status": "healthy"
    }