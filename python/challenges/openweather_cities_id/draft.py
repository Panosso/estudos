import config

total_cities = len(config.Config.CITY_IDS)

a = [{'user_id': '1', 'city_id': 3439525, 'temperature_celsius': 26.84, 'humidity': 53}, {'user_id': '1', 'city_id': 3439781, 'temperature_celsius': 24.37, 'humidity': 59}, {'user_id': '1', 'city_id': 3440645, 'temperature_celsius': 28.99, 'humidity': 25}, {'user_id': '1', 'city_id': 3442098, 'temperature_celsius': 24.93, 'humidity': 44}, {'user_id': '1', 'city_id': 3442778, 'temperature_celsius': 25.23, 'humidity': 44}, {'user_id': '1', 'city_id': 3443341, 'temperature_celsius': 26.81, 'humidity': 32}, {'user_id': '1', 'city_id': 3442233, 'temperature_celsius': 22.9, 'humidity': 59}, {'user_id': '1', 'city_id': 3440781, 'temperature_celsius': 25.17, 'humidity': 99}, {'user_id': '1', 'city_id': 3441572, 'temperature_celsius': 25.13, 'humidity': 44}, {'user_id': '1', 'city_id': 3441575, 'temperature_celsius': 25.01, 'humidity': 44}, {'user_id': '1', 'city_id': 3443207, 'temperature_celsius': 25.06, 'humidity': 44}, {'user_id': '1', 'city_id': 3442546, 'temperature_celsius': 24.91, 'humidity': 36}, {'user_id': '1', 'city_id': 3441287, 'temperature_celsius': 27.44, 'humidity': 32}, {'user_id': '1', 'city_id': 
3441242, 'temperature_celsius': 26.94, 'humidity': 61}, {'user_id': '1', 'city_id': 3441686, 'temperature_celsius': 27.06, 'humidity': 34}, {'user_id': '1', 'city_id': 3440639, 'temperature_celsius': 29.21, 'humidity': 24}, {'user_id': '1', 'city_id': 3441354, 'temperature_celsius': 
23.05, 'humidity': 68}, {'user_id': '1', 'city_id': 3442057, 'temperature_celsius': 24.84, 'humidity': 44}, {'user_id': '1', 'city_id': 3442585, 'temperature_celsius': 26.5, 'humidity': 37}, {'user_id': '1', 'city_id': 3442727, 'temperature_celsius': 24.97, 'humidity': 57}]

progress = (len(a) / total_cities) * 100

print(f"{progress:.2f}%")