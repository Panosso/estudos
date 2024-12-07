from fastapi import APIRouter
from .handlers.user import user_router
from api.auth.jwt import auth_router

#Centralizador de rotas
router = APIRouter()

router.include_router(user_router, 
                      prefix='/users',
                      tags=['users'])

router.include_router(auth_router,
                      prefix='/auth',
                      tags=['users'])

