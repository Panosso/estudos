from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from config import settings
from models import TokenData

fake_users_db = {
    "user": {"username": "user", "role": "user", "password": "L0XuwPOdS5U", "fullname": "Pedro Machado"},
    "admin": {"username": "admin", "role": "admin", "password": "JKSipm0YH", "fullname": "Panosso"}
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def verify_password(plain_password, hashed_password):
    return plain_password == hashed_password

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user_dict

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user or not verify_password(password, user["password"]):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        print(payload)
        username: str = payload.get("sub")
        role: str = payload.get("role")
        fullname: str = payload.get("fullname")
        if username is None or role is None:
            raise credentials_exception
        token_data = TokenData(username=username, role=role, fullname=fullname)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return token_data

def get_current_active_user(current_user: TokenData = Depends(get_current_user)):
    return current_user