import requests

def get_weather(url,city_name, api_key):
    params = {
        'q': city_name,
        'appid': api_key, 
        'units': 'metric',  # সেলসিয়াসে দেখাবে
        'lang': 'bn'        # বাংলায় আবহাওয়া বর্ণনা
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        print(f"\n📍 শহর: {city}")
        print(f"🌤️ আবহাওয়া: {weather}")
        print(f"🌡️ Tempareture: {temp}°C (অনুভব: {feels_like}°C)")
        print(f"💧 আর্দ্রতা: {humidity}%")
    else:
        print("❌ City information not found. Please enter the name correctly.")


# 🔑 নিজের API Key বসাও
base_url = "https://api.openweathermap.org/data/2.5/weather"  #From OpenWeatherMap APP 
api_key = "5a68f249fd2cd34161ebdfb432ddd41f" #From OpenWeatherMap APP 
city = input("🔍 আবহাওয়া দেখতে শহরের নাম লিখুন: ")
get_weather(base_url,city, api_key)
