import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',  # সেলসিয়াসে দেখাবে
        'lang': 'bn'        # বাংলায় আবহাওয়া বর্ণনা
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        print(f"\n📍 CITY: {city}")
        print(f"🌤️ Weather: {weather}")
        print(f"🌡️ Tempareture: {temp}°C (feels_like: {feels_like}°C)")
        print(f"💧 humidity: {humidity}%")
        
    else:
        print("❌ City information not found. Please enter the name correctly.")


# 🔑 নিজের API Key বসাও
api_key = "5a68f249fd2cd34161ebdfb432ddd41f"
city = input("🔍Please Type Your City Name: ")
get_weather(city, api_key)



# #For Test Code ................................................ 21)

# def use_test_purpose(city_name,api_key):
#     base_url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         'q': city_name,
#         'appid': api_key,
#         'units': 'metric',  # সেলসিয়াসে দেখাবে
#         'lang': 'bn'        # বাংলায় আবহাওয়া বর্ণনা
#     }

#     response = requests.get(base_url, params=params)
#     data = response.json()

#     result = {
#             "city": data['name'],
#             "weather": data['weather'][0]['description'],
#             "temp": data['main']['temp'],
#             "feels_like": data['main']['feels_like'],
#             "humidity": data['main']['humidity']
#         }
#     return result