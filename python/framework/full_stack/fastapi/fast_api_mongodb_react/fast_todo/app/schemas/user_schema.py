from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional


#Dados que serão solicitados para cadastro
class UserAuth(BaseModel):
    email: EmailStr = Field(..., description='E-mail Usuario')
    username: str = Field(..., min_length=5, max_length=50, description='Username usuario')
    hash_password: str = Field(..., min_length=5, max_length=20, description='Senha usuario')

#Dados que serão apresentados caso esteja tudo OK
class UserDetail(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool]
    
