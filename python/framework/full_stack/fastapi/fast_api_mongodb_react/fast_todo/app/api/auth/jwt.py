from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_services import UserService
from core.security import create_access_token, create_refresh_token
from schemas.auth_schema import TokenSchema
from schemas.user_schema import UserDetail
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from pydantic import ValidationError
from core.config import settings
from schemas.auth_schema import TokenPayload
from jose import jwt

auth_router = APIRouter()

@auth_router.post('/login', summary="Cria Access Token e Refresh token", response_model=TokenSchema)
#Esse OAuth2PasswordRequestForm, gera um formulario solicitando as informações do token, como username, senha e afins
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        username = data.username,
        password = data.password
    )
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email ou Senha incorretos'
        )

    return {
        "access_token" : create_access_token(usuario.user_id),
        "refresh_token": create_refresh_token(usuario.user_id)
    }

@auth_router.post('/test-token', summary='Teste de token', response_model=UserDetail)
#Esse depends força que a rota esteja autenticada.
async def test_token(user: User = Depends(get_current_user)):
    return user

@auth_router.post('/refresh', summary='Refresh Token', response_model=TokenSchema)
#Esse Body é uma textarea que aceita um text qualquer e pode user usado para passar o token
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_REFRESH_SECRET_KEY,
            settings.ALGORITHM
        )

        token_data = TokenPayload(**payload)

    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                    detail='Token Expirado',
                    headers={'WWW-Authenticate': 'Bearer'})
    
    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = 'Não foi possivel encontar o usuario',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    
    return {
        "access_token" : create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id)
    }
