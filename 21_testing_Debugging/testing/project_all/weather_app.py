import requests
import json

def get_weather_data(city_name, api_key):
    """
    OpenWeatherMap API theke weather data fetch kore.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None

def display_weather(weather_data):
    """
    Weather data print kore.
    """
    if weather_data and weather_data.get("cod") != "404":
        main_data = weather_data["main"]
        weather_description = weather_data["weather"][0]["description"]
        
        print(f"Weather in {weather_data['name']}:")
        print(f"  Description: {weather_description.capitalize()}")
        print(f"  Temperature: {main_data['temp']}°C")
        print(f"  Feels Like: {main_data['feels_like']}°C")
        print(f"  Humidity: {main_data['humidity']}%")
        print(f"  Pressure: {main_data['pressure']} hPa")
        return True
    else:
        print("Error: City not found or an issue occurred.")
        return False