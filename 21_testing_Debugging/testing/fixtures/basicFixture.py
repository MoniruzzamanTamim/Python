
def add_numbers(a,b):
    print("Add Number: ", a+b) 
    return a+b

def format_greeting(name):
    return f"Hello {name}"

add_numbers(1,20)

def add_item_to_list(my_list, item):
    """একটি লিস্টে একটি নতুন আইটেম যোগ করে।"""
    my_list.append(item)
    return my_list    


def get_user_info(user_dict, key):
    """একটি ডিকশনারি থেকে একটি নির্দিষ্ট কী-এর মান বের করে।"""
    return user_dict.get(key)

def read_file_content(file_path):
    """একটি ফাইল থেকে সব কন্টেন্ট পড়ে।"""
    with open(file_path, 'r') as f:
        return f.read()
    

def file_handle(path):

    with open(path, "w") as f:
        yield f
