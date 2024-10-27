import os

class Config:
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    CITY_IDS = []
    RATE_LIMIT = 60