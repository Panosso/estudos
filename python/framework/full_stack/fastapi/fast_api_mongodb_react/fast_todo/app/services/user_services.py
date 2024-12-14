from typing import Optional
from schemas.user_schema import UserAuth
from models.user_model import User
from core.security import get_password, verify_password

# JWT - Json Web Token

class UserService:
    
    @staticmethod
    async def create_user(user: UserAuth):
        usuario = User(
            username= user.username,
            email=user.email,
            hash_password=get_password(user.hash_password)
        )

        await usuario.insert()
        return usuario
    
    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user
    
    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[bool]:
        user = await UserService.get_user_by_email(email)

        if not user:
            return None
        
        elif not verify_password(
            password=password,
            hashed_password=user.hash_password
        ):
            return None
        
        else:
            return user
