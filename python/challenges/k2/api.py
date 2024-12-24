from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from models import Token, TokenData
from config import settings
import utils
import sqlite3


app = FastAPI()

@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = utils.authenticate_user(utils.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": f"{settings.TOKEN_TYPE}"},
        )
    access_token = utils.create_access_token(data={"sub": user["username"], "role": user["role"], "fullname": user["fullname"]})
    return {"access_token": access_token, "token_type": f"{settings.TOKEN_TYPE}"}

@app.get("/user")
def read_user_data(current_user: TokenData = Depends(utils.get_current_active_user)):
    if current_user.role != "user" or current_user.role == 'admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions"
        )
    return {"message": f"Hello {current_user.fullname}!", "user": current_user.username}

@app.get("/admin")
def read_admin_data(current_user: TokenData = Depends(utils.get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions"
        )
    return {"message": f"Hello {current_user.fullname}!", "admin": current_user.username}

@app.post("/data")
def create_data(content: str, current_user: TokenData = Depends(utils.get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions"
        )
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data (content) VALUES (?)", (content,))
    connection.commit()
    connection.close()
    return {"message": "Data created successfully!"}

@app.get("/data")
def read_data(current_user: TokenData = Depends(utils.get_current_active_user)):
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    connection.close()
    return {"data": rows}
