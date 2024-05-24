from fastapi import APIRouter

model_router = APIRouter(prefix="/models")


@model_router.get("/model_1")
async def get_model_1():
    return {
        "message": "1 Page"
    }


@model_router.get("/model_2")
async def get_model_2():
    return {
        "message": "2 Page"
    }


@model_router.get("/model_3")
async def get_model_3():
    return {
        "message": "3 Page"
    }