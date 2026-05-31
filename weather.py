import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

def fetch(city):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    respo = requests.get(url)
    data = respo.json()
    
    
    if str(data["cod"]) == "200":
    
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_condition = data['weather'][0]['description']
        feels_like = data["main"]["feels_like"]
        pressure = data["main"]["pressure"]

        wind_speed = data["wind"]["speed"]

        visibility = data["visibility"] / 1000   # meters -> km

        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S")
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")

        city_name = data["name"]
        country = data["sys"]["country"]
        return (
            city_name,
             country,
             temp,
            feels_like,
            humidity,
            pressure,
            sunrise,
            sunset,
            wind_speed,
            visibility,
            weather_condition
            )
    else :
        raise Exception("Data Not Fetch")

def main():
    try:
        city =input("Enter the city name:")
        city_name,country,temp,feels_like,humidity,pressure,sunrise,sunset,wind_speed,visibility,weather_condition = fetch(city)
        print(f"City: {city_name}")
        print(f"Country: {country}")
        print(f"Temperature: {temp} °C")
        print(f"Feels Like: {feels_like} °C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Sunrise:{sunrise}" )
        print(f"Sunset:{sunset}")      
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Visibility: {visibility} km")
        print(f"Condition: {weather_condition}")
    except Exception as e:
        print(str(e)) 

if __name__== "__main__":
     main()            