from fastapi import FastAPI
from auth import auth_router
from models import model_router
app = FastAPI()
app.include_router(auth_router)
app.include_router(model_router)


@app.get("/")
async def tset_1():
    return {
        "message": "My first easy example with fastapi"
    }

