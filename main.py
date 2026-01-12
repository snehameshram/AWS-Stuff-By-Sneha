import json
from datetime import datetime, timezone, timedelta
import pandas as pd 
import requests

city_name = 'Pune'
base_url = 'https://api.openweathermap.org/data/2.5/weather?q='

with open("credential.txt", "r") as f:
    api_key = f.read().strip()

full_url = f"{base_url}{city_name}&appid={api_key}"

r = requests.get(full_url)
print(r.status_code)
# print(r.text)

data = r.json()
# print(data)

def kelvin_to_fahrenheit(temp_in_kelvin):
    temp_in_fahrenheit = (temp_in_kelvin - 273.15) * (9/5) + 32
    return temp_in_fahrenheit

def etl_weather_data(url):
    r = requests.get(url)
    data = r.json()
    # print(data)

    offset = timezone(timedelta(seconds=data['timezone']))


    city = data["name"]
    weather_description = data["weather"][0]['description']
    temp_farenheit = kelvin_to_fahrenheit(data["main"]["temp"])
    feels_like_farenheit= kelvin_to_fahrenheit(data["main"]["feels_like"])
    min_temp_farenheit = kelvin_to_fahrenheit(data["main"]["temp_min"])
    max_temp_farenheit = kelvin_to_fahrenheit(data["main"]["temp_max"])
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    time_of_record = datetime.fromtimestamp(data['dt'], tz=timezone.utc).astimezone(offset)
    sunrise_time   = datetime.fromtimestamp(data['sys']['sunrise'], tz=timezone.utc).astimezone(offset)
    sunset_time    = datetime.fromtimestamp(data['sys']['sunset'], tz=timezone.utc).astimezone(offset)


    transformed_data = {"City": city,
                        "Description": weather_description,
                        "Temperature (F)": temp_farenheit,
                        "Feels Like (F)": feels_like_farenheit,
                        "Minimun Temp (F)":min_temp_farenheit,
                        "Maximum Temp (F)": max_temp_farenheit,
                        "Pressure": pressure,
                        "Humidty": humidity,
                        "Wind Speed": wind_speed,
                        "Time of Record": time_of_record,
                        "Sunrise (Local Time)":sunrise_time,
                        "Sunset (Local Time)": sunset_time                        
                        }

    transformed_data_list = [transformed_data]
    df_data = pd.DataFrame(transformed_data_list)
    # print(df_data)

    df_data.to_csv("current_weather_data_portland.csv", index = False)

if __name__ == '__main__':
    etl_weather_data(full_url)