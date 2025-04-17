import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables from .env file
load_dotenv()

# Function to save weather data to a JSON file
def save_to_json(city, data):
    with open(f"{city}_weather.json", "w") as file:
        json.dump(data, file, indent=4)  # Save data with indentation
    print(f"Weather data saved to {city}_weather.json")

# Function to get weather data
def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")  # Fetch the API key from environment
    if not api_key:
        print("API key not found!")
        return

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Temperature in Celsius
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\nWeather in {city}:")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"☁️ Condition: {data['weather'][0]['description'].title()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")

        # Save weather data to a JSON file
        save_to_json(city, data)  # Call function to save data to JSON file
    else:
        print("City not found or something went wrong!")

# === Program Start ===
city_name = input("Enter city name: ")
get_weather(city_name)

