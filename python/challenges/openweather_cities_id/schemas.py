from datetime import datetime
from pydantic import BaseModel, JsonValue


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
    openweather_json: JsonValue


class OpenWeatherStoreJSONCreate(OpenWeatherStoreJSONBase):
    pass


class OpenWeatherStoreJSON(OpenWeatherStoreJSONBase):
    id: int

    class Config:
        from_attributes = True