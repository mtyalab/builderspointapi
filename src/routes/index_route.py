from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"code": 200, "message": "qwix"}
