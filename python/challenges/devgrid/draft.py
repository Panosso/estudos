import os
from config import Config

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not OPENWEATHER_API_KEY:
    os.environ['OPENWEATHER_API_KEY'] = '1da566375b5c0306e294b682a45249b0'

abc = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}"

print('\n')
print(abc.format(lat = 50, lon = 40, API_key = Config.OPENWEATHER_API_KEY))