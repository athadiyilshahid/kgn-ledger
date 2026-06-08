from fastapi import FastAPI

from app.database import engine, Base

# Routers
from app.routers import auth, users, sales, purchases, expenses, ledger


# =========================
# CREATE DATABASE TABLES
# =========================
# (safe for development only)
Base.metadata.create_all(bind=engine)


# =========================
# FASTAPI APP
# =========================

app = FastAPI(
    title="Kgn Ledger API",
    description="Accounting Backend for Sales, Purchases, Expenses & Ledger",
    version="1.0.0"
)


# =========================
# ROUTERS
# =========================

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(sales.router)
app.include_router(purchases.router)
app.include_router(expenses.router)
app.include_router(ledger.router)


# =========================
# HEALTH CHECK
# =========================

@app.get("/")
def root():
    return {
        "message": "Kgn Ledger API is running 🚀"
    }