from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON, Float
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class User(Base):

    __tablename__ = 'DG_Users'

    id = Column('id', Integer, primary_key = True)
    name = Column('name', String, nullable = False)
    email = Column('email', String, nullable = False)
    password = Column('password', String, nullable = False)


class OpenWeatherStoreJSON(Base):

    __tablename__ = 'DG_OpenWeatherStoreJSON'

    id = Column('id', Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("DG_Users.id"))
    request_date = Column(DateTime, nullable=False)
    openweather_json = Column(JSON, nullable=False)
    temperature_celsius = Column(Float, nullable=False, default=0)

class ProgressResponse(Base):
    user_id = Column(Integer, ForeignKey("DG_Users.id"))
    complete_percentage = Column(Float, nullable=False, default=0)