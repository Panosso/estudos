from datetime import datetime
from pydantic import BaseModel, Json


class UserBase(BaseModel):

    name: str
    email: str
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True



class OpenWeatherStoreJSONBase(BaseModel):

    user_id: int
    request_date: datetime
    openweather_json: str


class OpenWeatherStoreJSONCreate(OpenWeatherStoreJSONBase):
    pass


class OpenWeatherStoreJSON(OpenWeatherStoreJSONBase):
    id: int

    class Config:
        from_attributes = True