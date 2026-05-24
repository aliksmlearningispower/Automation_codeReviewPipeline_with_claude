from fastapi import FastAPI

# Create the FastAPI instance
app = FastAPI()

password = "admin123_113"

def divide(a,b):
    return a/b

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Gnani nerchukuntu jeevinch apai gnaname nennu poshinchu, Rakshinchu, meruguparuchu, balaparuchu and lot many more"}

# Endpoint with a path parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query_param": q}