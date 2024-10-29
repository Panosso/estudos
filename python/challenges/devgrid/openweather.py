from requests import get as rget
from datetime import datetime
from os import getenv
from config import Config

import logging


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

class OpenWeatherClass:

    @staticmethod
    def check_lat_lon(latitude: float, longitude: float):
        return -90 <= latitude <= 90 and -180 <= longitude <= 180
    
    @classmethod
    def get_city_info(_, city_id: str, api_key: str, units='metric'):

        try:

            info = ''
            city_id = f"id={city_id}"
            appid = f"&appid={api_key}"
            units = f"&units={units}"

            request = Config.BASE_URL_WEATHER+ '?' + city_id + units + appid

            response = rget(request)

            if response.status_code == 200:
                info = response.json()

            else:
                info = f'Nothing found, reason: {response.json()}'

        except Exception as e:

            info = {'erro': f"Erro encontrado: {e}.", "erro_cod": -1}

            return info

        return info
    
    @classmethod
    def get_city_info_lat_lon(self, lat, lon):

        # if self.check_lat_lon(lat, lon):
        request = Config.BASE_URL_WEATHER.format(lat = lat, lon = lon, API_key = Config.OPENWEATHER_API_KEY)
        logger.debug(request)
        response = rget(request)

        logger.debug(response)

        if response.status_code == 200:
            info = response.json()

        logger.debug(info)