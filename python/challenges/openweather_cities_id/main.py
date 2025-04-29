import hashlib
import asyncio
import crud
import models
import schemas
import utils
import logging
import config

from datetime import datetime, timedelta
from fastapi import (Depends, FastAPI, HTTPException, responses,
                     status)
from sqlalchemy.orm import Session
from typing import Union

from database import SessionLocal, engine
from openweather import OpenWeatherClass, weather_collect_data

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
now = datetime.now()

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

weather_service = OpenWeatherClass(api_key=config.Config.OPENWEATHER_API_KEY)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_user/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate,
                      db: Session = Depends(get_db)):
    
    if not utils.email_validator(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email format.")

    email = crud.get_user_by_email(db, user_email = user.email)
    if email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already in use.")

    user.password = hashlib.sha3_256(f'{user.password}'.encode('UTF-8')).hexdigest()

    crud.create_user(db=db, user=user)

    res = {
        'User': f'{user.email} was created successfully',
    }

    return responses.JSONResponse(content=res)

@app.get('/user/', response_model=schemas.User)
async def get_user(user_email: str,
                   db: Session = Depends(get_db)):

    user = crud.get_user_by_email(db, user_email)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    
    return user

@app.get('/user/logging/', response_model=schemas.User)
async def log_user(user_email: str,
                   user_passwd: str,
                   db: Session = Depends(get_db)):
    
    user = crud.get_user_by_email(db, user_email)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Email not found")
    
    user_passwd = hashlib.sha3_256(f'{user_passwd}'.encode('UTF-8')).hexdigest()

    if user_passwd != user.password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Password not found")
    user.is_loggin = True
    user.date_to_log_active = datetime.now() + timedelta(hours=3)
    
    crud.update_user(db=db, user_new_value=user)
    
    res = {
        'User': f'{user.name} was log in',
    }

    return responses.JSONResponse(content=res)

@app.post('/weather/', response_model=schemas.OpenWeatherStoreJSON)
async def post_weather(user_id: str,
                       db: Session = Depends(get_db)):
    
    user = crud.get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")

    if utils.is_not_authorized(user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User need to be Log In")
    
    await weather_service.weather_jsons(user_id=user_id, 
                                        db=db)
    
    res = {"status": "Weather data collection started."}

    return responses.JSONResponse(content=res)

@app.get('/weather/process_percentage/')
def get_process_percentage(user_id: str,
                           db: Session = Depends(get_db)):

    try:
        user = crud.get_user_by_id(db, user_id)

        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="User not found")

        if utils.is_not_authorized(user):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="User need to be Log In")

        total_cities = len(config.Config.CITY_IDS)
        collect_citys = len(weather_collect_data[user_id])

        progress = (collect_citys / total_cities) * 100

        res = {"user_id": user_id, "completion_percentage": f"{progress:.2f}%"}

        return responses.JSONResponse(content=res)
    
    except Exception as e:

        err = {'Error': f"{e}"}

        return responses.JSONResponse(err)