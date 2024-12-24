from fastapi import APIRouter, HTTPException, status
import pymongo.errors
from schemas.user_schema import UserAuth, UserDetail
from services.user_services import UserService
import pymongo

user_router = APIRouter()

@user_router.post("/adicionar", summary='Adicionar usuario', response_model=UserDetail)
async def adiciona_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username ou Email ja estão sendo utilizados"
        )
