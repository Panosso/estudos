from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_services import UserService
from core.security import create_acess_token, create_refresh_token
from schemas.auth_schema import TokenSchema

auth_router = APIRouter()

@auth_router.post('/login', summary="Cria Access Token e Refresh token", response_model=TokenSchema)
#Esse OAuth2PasswordRequestForm, gera um formulario solicitando as informações do token, como username, senha e afins
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    print(data.username)
    print(data.password)
    usuario = await UserService.authenticate(
        email= data.username,
        password = data.password
    )

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email ou Senha incorretos'
        )

    return {
        "acess_token": create_acess_token(usuario.user_id),
        "refresh_token": create_refresh_token(usuario.user_id)
    }
