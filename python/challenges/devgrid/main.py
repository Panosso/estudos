import hashlib
from tqdm import tqdm
from time import sleep
from random import randint
from datetime import datetime
from fastapi import (Depends, FastAPI, HTTPException, responses,
                     status)
from sqlalchemy.orm import Session
from typing import Union, List

import crud
import models
import schemas
import utils
import logging
from database import SessionLocal, engine
from openweather import OpenWeatherClass

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
now = datetime.now()

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_user/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate,
                      db: Session = Depends(get_db)):
    

    if utils.email_validator(user.email):
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

@app.post("/save_info/")
async def read_climate(user_id: int,
                 api_key: str,
                 q: Union[str, None] = None,
                 db: Session = Depends(get_db)):

    user = crud.get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")

    json_response = {}
    jsons_list = []

    logger

    cities_ids = q.replace(' ', '').split(',')

    for i in tqdm(range (0, len(cities_ids)), desc="Loading"):

        city_id123 = cities_ids[i]

        logger.debug(city_id123)

        location_info = OpenWeatherClass.get_city_info(city_id = city_id123,
                                api_key = api_key)

        if 'erro_cod' in location_info.keys():

            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Information not found")
        
        else:

            city_name = location_info["name"]
            json_response["temp_C"] = round(location_info['main']['temp'])
            json_response["humidity"] = location_info['main']['humidity']
            json_response["city_id"] = location_info['id']
            json_response["requestdate"] = utils.convert_datetime_utc()
            json_response["user_id"] = user.id

            jsons_list.append({city_name: json_response})

            save_info = schemas.OpenWeatherStoreJSONCreate(user_id=user.id, 
                                                request_date=json_response["requestdate"],
                                                openweather_json=str(json_response))
            crud.create_citie_info(db, openweatherstorejson=save_info)

        json_response = {}

        sleep(randint(3, 9))

    return {'Process completed': jsons_list}

@app.get('/user/{user_email}', response_model=schemas.User)
async def get_user(user_email: str,
                   db: Session = Depends(get_db)):

    user = crud.get_user_by_email(db, user_email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    
    return user

@app.get('/city_info_lat_lon/')
async def get_city_info_lat_lon(q: Union[str, None] = None,):
    try:
        
        lat, lon = q.replace(' ', '').split(',')

        info = OpenWeatherClass.get_city_info_lat_lon(lat, lon)
        
        return info

    except Exception as e:
        pass


@app.get('/process_percentage/', response_model=schemas.OpenWeatherStoreJSON)
def get_process_percentage():
    pass