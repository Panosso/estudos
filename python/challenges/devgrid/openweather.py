import asyncio
import config
import requests
import random
import logging
import crud
import schemas

from requests import get as rget
from datetime import datetime

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

weather_collect_data = {}

class OpenWeatherClass:

    def __init__(self, api_key):
        self.api_key = api_key
    
    async def get_jsons(self, city_id):

        request = "https://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&appid=1da566375b5c0306e294b682a45249b0"
        result = requests.get(request.format(city_id=city_id)).json()

        return result

    async def weather_jsons(self, user_id, db):

        timestamp = datetime.now()
        collected_jsons = []
        for i in range(0, len(config.Config.CITY_IDS), config.Config.RATE_LIMIT):
            tasks = [self.get_jsons(city_id) for city_id in config.Config.CITY_IDS[i:i + config.Config.RATE_LIMIT]]

            jsons = await asyncio.gather(*tasks)
    
            for json in jsons:
                data = {
                        'user_id': user_id,
                        'city_id': json['id'],
                        'temperature_celsius': json['main']['temp'],
                        'humidity': json['main']['humidity']
                    }

                collected_jsons.append(data)
                weather_collect_data[user_id] = collected_jsons
                
                logger.debug('Estou dormindo')
                logger.debug(weather_collect_data)
                await asyncio.sleep(60)
                logger.debug('Estou dormindo')

            json_schema = schemas.OpenWeatherStoreJSONCreate(openweather_json=collected_jsons, user_id=user_id, request_date=timestamp)

            crud.create_citie_info(db, json_schema)












    # async def get_weather_city(self, city_id: int):
    #     async with aiohttp.ClientSession() as session:
    #             for city in config.Config.CITY_IDS:
    #                 open_weather_url = f"http://api.openweathermap.org/data/2.5/weather?id={city}&appid={config.Config.OPENWEATHER_API_KEY}&units=metric"
    #                 async with session.get(open_weather_url) as resp:
    #                     return await resp.json()

    # async def collect_weather_data(self, user_id: str):
    #     collect_data = []
    #     timestamp = datetime.now()
    #     for i in range(0, len(Config.CITY_IDS)):
    #         tasks = [self.get_weather_city(city_id) for city_id in Config.CITY_IDS[i:i + Config.RATE_LIMIT]]
    #         results = await asyncio.gather(*tasks)
    #         for result in results:

    #             data = {
    #                 'user_id': user_id,
    #                 'timestamp': timestamp,
    #                 'city_id': result['id'],
    #                 'temperature_celsius': result['main']['temp'],
    #                 'humidity': result['main']['humidity']
    #             }

    #             collect_data.append(data)
    #             weather_data_storage[user_id] = data
    #         await asyncio.sleep(10)