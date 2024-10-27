from  openweather import OpenWeatherClass

class TestClass:

    def test_check_lat_lon_return_True_with_latitude_50_and_longitude_100(self):
        waited_result = True

        result = OpenWeatherClass.check_lat_lon(50, 100)

        assert result == waited_result

    def test_get_city_info_pass_city_id_api_key_units_return_rib_preto_info(self):
        waited_result = '''{
                "coord": {
                    "lon": -47.8103,
                    "lat": -21.1775
                },
                "weather": [
                    {
                        "id": 802,
                        "main": "Clouds",
                        "description": "scattered clouds",
                        "icon": "03n"
                    }
                ],
                "base": "stations",
                "main": {
                    "temp": 26.51,
                    "feels_like": 26.51,
                    "temp_min": 26,
                    "temp_max": 26.51,
                    "pressure": 1010,
                    "humidity": 64,
                    "sea_level": 1010,
                    "grnd_level": 941
                },
                "visibility": 10000,
                "wind": {
                    "speed": 4.12,
                    "deg": 70
                },
                "clouds": {
                    "all": 40
                },
                "dt": 1729978546,
                "sys": {
                    "type": 2,
                    "id": 2095490,
                    "country": "BR",
                    "sunrise": 1729931487,
                    "sunset": 1729977518
                },
                "timezone": -10800,
                "id": 3451328,
                "name": "Ribeirão Preto",
                "cod": 200
            }'''

        result = OpenWeatherClass.get_city_info(3451328, '1da566375b5c0306e294b682a45249b0', 'metric')
        
        assert waited_result == result
