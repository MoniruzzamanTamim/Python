import requests # Importing the requests library for making HTTP requests
import threading # Importing the threading library for multithreading
import json # Importing the json library for handling JSON data


# Function to POST  data from a given URL and print the JSON response
# fetch_data function ----POST METHOD.....................................................................................................................................
def postData(url, data=None):
    reponse = requests.post(url, json = data) # Making a POST request to the URL
    print(f"Status Code: {reponse.status_code}") # Printing the status code of the response
    print(f"Response: {reponse.json()}") # Printing the JSON response from the server

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Tamim's post",
    "body": "This is a test",
    "userId": 101,
    "id": 101
}
postData(url, data) # Fetching data from the specified URL
print("Post  data from successfully completed!")

# fetch_data function ----GET  METHOD.....................................................................................................................................
# def getData(url):
#     response = requests.get(url) # Making a GET request to the URL
#     if response.status_code == 200: # Checking if the request was successful    
#         print(f"Data fetched from {url}:")
#         json_data = response.json() # Parsing the JSON response
#         for  data in json_data:
#             if data['id'] ==  11:
#                 print(f"ID: {data['id']}, Title: {data['title']}, Body: {data['body']}") # Printing the ID, Title, and Body of the post
#                 break
#             else:
#                 print("Your Data Not Avail able" ) 
#     else:
#         print(f"Failed to fetch data from {url}, Status Code: {response.status_code}")

# url = "https://jsonplaceholder.typicode.com/posts"
# getData(url)
