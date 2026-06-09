from fastapi import FastAPI

from app.database import Base, engine
from app import models  # IMPORTANT: ensures all tables are registered

from app.routers import users, sales, purchases, expenses, ledger

app = FastAPI(title="KGN Ledger API")


# -------------------------------------------------
# FORCE TABLE CREATION (RUNS ON IMPORT, NOT EVENT)
# -------------------------------------------------
Base.metadata.create_all(bind=engine)


# -----------------------------
# Register routers
# -----------------------------
app.include_router(users.router)
app.include_router(sales.router)
app.include_router(purchases.router)
app.include_router(expenses.router)
app.include_router(ledger.router)


# -----------------------------
# Health check route
# -----------------------------
@app.get("/")
def root():
    return {"message": "KGN Ledger API is running"}