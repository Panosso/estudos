from requests import get as rget
from datetime import datetime
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class OpenWeatherClass:

    @staticmethod
    def check_lat_lon(latitude: float, longitude: float):
        return -90 <= latitude <= 90 and -180 <= longitude <= 180
    
    @classmethod
    def get_city_info(_, city_id, api_key, units='metric'):

        try:

            info = ''
            #https://api.openweathermap.org/data/2.5/weather?id=3443952&units=metric&appid=1da566375b5c0306e294b682a45249b0
            api_base = f"https://api.openweathermap.org/data/2.5/weather?"
            city_id = f"id={city_id}"
            appid = f"&appid={api_key}"
            units = f"&units={units}"

            request = api_base + city_id + units + appid

            print(request)

            response = rget(request)

            if response.status_code == 200:
                info = response.json()

            else:
                info = f'Nothing found, reason: {response.json()}'

        except Exception as e:

            info = {'erro': f"Erro encontrado: {e}.", "erro_cod": -1}

            return info

        return info
    