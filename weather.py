import requests
import json
import time
import datetime
import os
import pyfiglet

# Put your key here
KEY = ""

# Grep lat and lon from the city name 
def city_info(city):
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}'
    request = requests.get(URL)
    data = request.json()
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    return lat, lon

        
def main():
    while True:
        os.system('cls')
        ascii_art = pyfiglet.figlet_format("Weather v1.0")
        print(ascii_art)
        print("-" * 60)
        city = input("Enter the city name (q to quit): ")
        if city.lower() == 'q':
            print("Goodbye!")
            time.sleep(2)
            break
        print("-" * 60)
        try:
            lat = city_info(city)[0]
            lon = city_info(city)[1]
        except KeyError:
            print("City not found!")
            print("Please enter the correct city name")
            time.sleep(2)
            continue

        URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}'
        request = requests.get(URL)
        data = request.json()

        with open('weather.json', 'w') as file:
            json.dump(data, file, indent=4)

        # Weather data
        weather = data["weather"][0]['main']
        weather_description = data["weather"][0]['description']

        # Temprature and humidity data
        temprature_kelvin = (data["main"]['temp'])
        temprature_celsius = temprature_kelvin - 273.15
        temprature = f"{temprature_celsius:.2f}"
        humidity = data["main"]['humidity']

        # Wind data
        wind_speed = data["wind"]['speed']

        # Clouds data
        clouds = clouds = data["clouds"]['all']

        print(f"""
    - Weather: {weather} ({weather_description})
    - Temprature: {temprature}°C           - Humidity: {humidity}%
    - Wind Speed: {wind_speed} m/s
    - Clouds: {clouds}%

------------------------------------------------------------
        """)
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() == 'n':
            print("Goodbye!")
            time.sleep(2)
            break
        elif choice.lower() == 'y':
            continue

if __name__ == "__main__":
    main()
