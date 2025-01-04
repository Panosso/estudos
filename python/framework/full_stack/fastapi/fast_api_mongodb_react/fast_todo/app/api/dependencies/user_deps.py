from fastapi.security import OAuth2PasswordBearer
from core.config import settings
from fastapi import Depends, HTTPException, status
from models.user_model import User
from jose import jwt
from schemas.auth_schema import TokenPayload
from datetime import datetime
from pydantic import ValidationError
from services.user_services import UserService

oauth_reusavel = OAuth2PasswordBearer(tokenUrl = f"{settings.API_V1_STR}/auth/login", scheme_name="JWT")

async def get_current_user(token: str = Depends(oauth_reusavel)) -> User:
    try:

        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            settings.ALGORITHM
        )

        #token data
        token_data = TokenPayload(**payload)
        print(token_data)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Token Expirado',
                                headers={'WWW-Authenticate': 'Bearer'})

    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code= status.HTTP_403_FORBIDDEN,
            detail='Erro na validação',
            headers={'WWW-Authenticate': 'Bearer'}
            )
    
    except Exception as e:
        raise HTTPException(
            detail = f'Erro {e}',
            headers = {'WWW-Authenticate': 'Bearer'}
        )
    
    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = 'Não foi possivel encontar o usuario',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    

    return user