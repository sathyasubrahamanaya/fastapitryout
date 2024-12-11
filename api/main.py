from fastapi import FastAPI

from product_management.manage_product import product_router


app = FastAPI()
app.include_router(product_router)


