import threading
import time

# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")
#         time.sleep(1)

# def print_letters():
#     for letter in ['A', 'B', 'C', 'D', 'E']:
#         print(f"Letter: {letter}")
#         time.sleep(1)

# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_letters)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Done!")



# #With Argument 

# def print_numbers(start, end):
#     for i in range(start, end):
#         print(f"Number: {i}")
#         time.sleep(1)   

# def print_letters(letters):
#     for letter in letters:
#         print(f"Letter: {letter}")
#         time.sleep(1)

# t1 = threading.Thread(target=print_numbers, args=(0, 5))
# t2 = threading.Thread(target=print_letters, args=(['A', 'B', 'C', 'D', 'E'],))  
# t1.start()
# t2.start()  
# t1.join()
# t2.join()           
# print("Done!")


# list1 = [1, 2, 3, 4, 5]
# list2 = ['A', 'B', 'C', 'D', 'E']
# def print_list_elements(lst):
#     for element in lst:
#         print(f"Element: {element}")
#         time.sleep(1)
# t3 = threading.Thread(target=print_list_elements, args=(list1,))
# t4 = threading.Thread(target=print_list_elements, args=(list2,))    
# t3.start()
# t4.start()  
# t3.join()
# t4.join()       
# print("All threads completed!")




#Project---------------------------------------------------------------------

import threading
import requests
import time
import json
# ✅ এই ফাংশনটি নির্দিষ্ট URL থেকে ডেটা আনে
def fetch_data(url):
    print(f"Fetching from {url}")
    response = requests.get(url)
    print(f"Done fetching {url}, Status Code: {response.status_code}")
# ✅ একাধিক API URL লিস্ট
urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/todos"
]
# ✅ থ্রেড লিস্ট তৈরি
threads = []
start_time = time.time()
# ✅ প্রতিটি URL এর জন্য একটা থ্রেড তৈরি করা হচ্ছে
for url in urls:
    t = threading.Thread(target=fetch_data, args=(url,))
    t.start()
    threads.append(t)

# ✅ সব থ্রেড শেষ না হওয়া পর্যন্ত অপেক্ষা
for t in threads:
    t.join()
end_time = time.time()
print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")


##Project----------------------------------------------------------------------------------------------------------

# #Fetch Data from API and Print JSON Data
# # ✅ এই ফাংশনটি নির্দিষ্ট URL থেকে ডেটা আনে এবং JSON ডেটা প্রিন্ট করে
# url  = "https://jsonplaceholder.typicode.com/posts"

# def fetch_data(url):
#     print(f"Fetching from {url}")
#     response = requests.get(url)
#     if response.status_code == 200:
#         print(f"Done fetching {url}, Status Code: {response.status_code}")
#         json_data = response.json()
#         for post in json_data[:20]:  # Limiting to first 20 posts for brevity
#             # ✅ প্রতিটি পোস্টের ID, Title এবং Body প্রিন্ট করা হচ্ছে    
#             print(f"Post ID: {post['id']}, Title: {post['title']}, \nBody: {post['body']}") 
#     else:
#         print(f"Failed to fetch {url}, Status Code: {response.status_code}")

# fetch_data(url)