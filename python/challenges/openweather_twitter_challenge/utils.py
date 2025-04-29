
def get_temp_list(dates, json_forecast):

    jsons = {}
    for date in dates:
        date = date.strftime('%Y-%m-%d')

        if not date in jsons.keys():
            jsons[date] = []

        for i in json_forecast["list"]:
            if date in i['dt_txt']:
                jsons[date].append(i['main']['temp'])

    return jsons

def convert_to_celcius(temp):
    temp = round(temp - 273.15, 0)
    return temp