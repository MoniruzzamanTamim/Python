#Q4. https://api.agify.io?name=michael এই API ব্যবহার করে ইউজারের নাম ইনপুট নিয়ে তার বয়স অনুমান করো।

import requests 
import json
def guessAge(name):
    try:
        params = {
            'name': name, 
            'country_id':  "BD"}
        base_url = "https://api.agify.io"
    except Exception as e :
        print("Error: ", e)
    try:
        response = requests.get(base_url, params= params)
        print("response.status_code  ",response.status_code)
        if response.status_code == 200:
            data = response.json()
            info = f"Code: {data['count']} || Name: {name} || Age: {data['age']} ||  Country: {data["country_id"]} "
            print(info)
        else: 
            print(response.status_code)
    except Exception as e:
        print("Error:", e)


name = input("Type Your Name: ").lower()
guessAge(name)