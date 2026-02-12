from fastapi import FastAPI
import dal

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hellthy"}

@app.get("/analytics/top-customers")
async def top_costumers():
    return dal.top_costumers()

@app.get("/analytics/customers-without-orders")
async def customers_without_orders():
    return dal.customers_without_orders()
@app.get("/analytics/zero-credit-active-customers")
async def zero_credit_active_customers():
    return dal.zero_credit_active_customers()