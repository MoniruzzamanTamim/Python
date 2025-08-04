import requests # Importing the requests library for making HTTP requests
import threading # Importing the threading library for multithreading
import json # Importing the json library for handling JSON data

# Function to fetch data from a given URL and print the JSON response
# fetch_data function ----GET METHOD 
def getData(url):
    response = requests.get(url) # Making a GET request to the URL
    if response.status_code == 200: # Checking if the request was successful    
        print(f"Data fetched from {url}:")
        print(json.dumps(response.json()[:10], indent=4)) # Printing the JSON response in a pretty format
    else:
        print(f"Failed to fetch data from {url}, Status Code: {response.status_code}")
# Main function to demonstrate fetching data from multiple URLs using threads
def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    getData(url) # Fetching data from the specified URL
    print("\nFetching data from successfully completed!")

main() # Calling the main function to execute the code
