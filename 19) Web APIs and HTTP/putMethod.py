import requests
import json 

def putData(url,data):
    response = requests.put(url, json = data)
    print("Some Information update Successfully .................")
    print(f"Response Data: {response.json()}")
    print("Response Code:" , response.status_code)

url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
   "userId": 2,
  "id": 11,
  "title": "Update Some Data ",
  "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus\naccusamus in eum beatae sit\nvel qui neque voluptates ut commodi qui incidunt\nut animi commodi"
}

putData(url, data)