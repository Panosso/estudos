from requests import get as rget
from datetime import datetime
from os import getenv


class OpenWeatherClass:

    @staticmethod
    def check_lat_lon(latitude: float, longitude: float):
        return -90 <= latitude <= 90 and -180 <= longitude <= 180
    
    @classmethod
    def get_city_info(city_id, api_key, units='metric'):

        try:

            info = ''
            api_base = f"https://api.openweathermap.org/data/2.5/weather?"
            city_id = f"id={city_id}"
            appid = f"&appid={api_key}"
            units = f"&units={units}"

            request = api_base + city_id + units + appid

            response = rget(request)

            if response.status_code == 200:
                info = response.json()

            else:
                info = f'Nothing found, reason: {response.json()}'

        except Exception as e:

            info = {'erro': f"Erro encontrado: {e}.", "erro_cod": -1}

            return info

        print('info')
        print(info)

        return info
    