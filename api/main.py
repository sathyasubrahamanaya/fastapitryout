from fastapi import FastAPI

app = FastAPI()

@app.get("/index")
def index():
    return {"name":"sathya","designation":"ML engineer"}