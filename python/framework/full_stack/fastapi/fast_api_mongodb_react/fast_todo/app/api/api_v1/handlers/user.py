from fastapi import APIRouter, HTTPException, status, Depends
from schemas.user_schema import UserAuth, UserDetail
from services.user_services import UserService
from models.user_model import User
from api.dependencies.user_deps import get_current_user

import pymongo.errors
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

@user_router.get('/me', summary='Detalhes do usuário logado', response_model=UserDetail)
async def get_me(user: User = Depends(get_current_user)):
    return user