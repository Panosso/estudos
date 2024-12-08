from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description='E-mail Usuario')
    username: str = Field(..., min_length=5, max_length=50, description='Username usuario')
    hash_password: str = Field(..., min_length=5, max_length=20, description='Senha usuario')

class UserDetail(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool]
    
