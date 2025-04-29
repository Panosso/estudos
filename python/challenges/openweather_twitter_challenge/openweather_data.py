import requests
import datetime
import asyncio
import os

from utils import convert_to_celcius, get_temp_list

class OpenWeatherData:

    def __init__(self, openweather_key):
        self.openweather_key = openweather_key
        self.open_url = f'https://api.openweathermap.org/data/2.5/forecast?'

    async def get_city_info(self, lat, lon):

        self.open_url += f'lat={lat}&lon={lon}&appid={self.openweather_key}'

        forecast = requests.get(self.open_url)

        json_forecast = forecast.json()

        weather = requests.get(self.open_url.replace('forecast', 'weather'))

        json_weather = weather.json()

        city_name = json_forecast['city']['name']
        main_weather = json_weather['weather'][0]['main']
        temp = convert_to_celcius(json_weather['main']['temp'])

        dates = []
        date_now = datetime.datetime.now()

        for i in range(5):
            dates.append(date_now + datetime.timedelta(days=i+1))

        temp_dict = get_temp_list(dates=dates, json_forecast=json_forecast)

        mean_text = await self.mean_temp_day(temp_dict)

        mean_text = self.generate_text(mean_text)

        text = f"{temp}°C e {main_weather} em {city_name} em {date_now.strftime('%d/%m')}. Média para os próximos dias: {mean_text}"

        return text

    async def mean_temp_day(self, dict_temp):

        results = []

        tasks = []

        for i in dict_temp:
            tasks.append(self.calculate_mean(i, dict_temp[i]))

        results = await asyncio.gather(*tasks)

        return results

    async def calculate_mean(self, date, lista):

        soma = 0
        lista_len = len(lista)
        media = 0

        for i in lista:
            soma += i

        media = round((soma/lista_len) - 273.15)

        date = datetime.datetime.strptime(date, "%Y-%m-%d")

        date = date.strftime('%d/%m')

        return (date, media)
        
    def generate_text(self, text_list):
        mean_text = ''
        range_text_list = len(text_list)
        for i in range(range_text_list):
            if i == range_text_list - 1:
                mean_text += f'e {text_list[i][1]}°C em {text_list[i][0]}'
            elif i == 0:
                mean_text += f'{text_list[i][1]}°C em {text_list[i][0]}'
            else:
                mean_text += f', {text_list[i][1]}°C em {text_list[i][0]}'

        return mean_text
