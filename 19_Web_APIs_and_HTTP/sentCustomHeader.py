import requests

def send_custom_headers():
    url = "https://httpbin.org/headers"
    
    headers = {
        "User-Agent": "TamimPracticeBot/1.0",
        "Authorization": "Bearer 12345",
        "X-Custom-Header": "HelloFromTamim"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("✅ Custom headers sent successfully.\n")
        json_data = response.json()
        
        # Header response print
        for key, value in json_data['headers'].items():
            print(f"{key}: {value}")
    else:
        print("❌ Request failed:", response.status_code)

# 🔍 Run
send_custom_headers()
