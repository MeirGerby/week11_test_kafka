from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/analytics/top-customers")
async def top_costumers():
    return {"message": "Hello World"}

@app.get("/analytics/customers-without-orders")
async def customers_without_orders():
    return {"message": "Hello World"}
@app.get("/analytics/zero-credit-active-customers")
async def zero_credit_active_customers():
    return {"message": "Hello World"}