from sqlalchemy.orm import Session

import models
import schemas

#DG_User table
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_new_value):
    user_id = user_new_value.id
    user = get_user_by_id(db = db, id=user_id)
    user.is_loggin = user_new_value.is_loggin
    user.date_to_log_active = user_new_value.date_to_log_active
    db.commit()

def get_user_by_email(db: Session, user_email: str):
    return db.query(models.User).\
        filter(models.User.email == user_email).first()

def get_user_by_id(db: Session, id: int):
    return db.query(models.User).\
        filter(models.User.id == id).first()


#DG_OpenWeatherStoreJSON
def create_citie_info(db: Session, openweatherstorejson: schemas.OpenWeatherStoreJSONCreate):
    db_openweatherstorejson = models.OpenWeatherStoreJSON(**openweatherstorejson.model_dump())
    db.add(db_openweatherstorejson)
    db.commit()
    db.refresh(db_openweatherstorejson)
    return db_openweatherstorejson
