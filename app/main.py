from fastapi import FastAPI

from app.routers import users, sales, purchases, expenses, ledger
from app.database import Base, engine
from app import models  # IMPORTANT: ensures models are registered before create_all

app = FastAPI(
    title="KGN Ledger API",
    version="1.0.0"
)


# ==============================
# CREATE TABLES ON STARTUP
# ==============================
@app.on_event("startup")
def startup():
    # create missing tables in production DB
    Base.metadata.create_all(bind=engine)


# ==============================
# ROUTERS
# ==============================
app.include_router(users.router)
app.include_router(sales.router)
app.include_router(purchases.router)
app.include_router(expenses.router)
app.include_router(ledger.router)


# ==============================
# HEALTH CHECK
# ==============================
@app.get("/")
def root():
    return {
        "message": "KGN Ledger API is running"
    }