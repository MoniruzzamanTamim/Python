
import requests
import threading    
import  json

def fetch_data(url):
    print("Fetching from", url)
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        print("Data fetched successfully:................................")  # Print first 10 items for brevity
        for post in json_data[:20]:  # Limiting to first 20 posts for brevity
#             # ✅ প্রতিটি পোস্টের ID, Title এবং Body প্রিন্ট করা হচ্ছে    
                print(f"Post ID: {post['id']}, Title: {post['title']}, \nBody: {post['body']}") 
    else:   
        print("Failed to fetch data:", response.status_code)    
        

url  = "https://jsonplaceholder.typicode.com/posts"
fetch_data(url)

