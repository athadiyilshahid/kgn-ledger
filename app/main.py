from fastapi import FastAPI

from app.routers import users, sales, purchases, expenses, ledger

app = FastAPI(title="KGN Ledger API")

# Register routers
app.include_router(users.router)
app.include_router(sales.router)
app.include_router(purchases.router)
app.include_router(expenses.router)
app.include_router(ledger.router)


@app.get("/")
def root():
    return {"message": "KGN Ledger API is running"}