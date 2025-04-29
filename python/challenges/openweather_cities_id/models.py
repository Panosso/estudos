from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON, Boolean, sql
from database import Base
from datetime import datetime


class User(Base):

    __tablename__ = 'DG_Users'

    id = Column('id', Integer, primary_key = True)
    name = Column('name', String, nullable = False)
    email = Column('email', String, nullable = False)
    password = Column('password', String, nullable = False)
    is_loggin = Column('loggin', Boolean, nullable=False, default=sql.expression.false())
    date_to_log_active = Column('date_limit_logging', DateTime, nullable=True, default=datetime.now())


class OpenWeatherStoreJSON(Base):

    __tablename__ = 'DG_OpenWeatherStoreJSON'

    id = Column('id', Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("DG_Users.id"))
    request_date = Column(DateTime, nullable=False)
    openweather_json = Column('JSONS', JSON, nullable=False)
