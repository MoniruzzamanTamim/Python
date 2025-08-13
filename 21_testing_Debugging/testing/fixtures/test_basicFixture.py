
import pytest
import os
from basicFixture  import add_numbers , format_greeting, add_item_to_list, get_user_info, read_file_content, file_handle


# @pytest.fixture #Create Fixute / Create Teamplete 
@pytest.fixture
def numbers():
    print("\nFixture: সংখ্যা pair তৈরি হচ্ছে (5, 10)")
    return 10,25  

def test_add_two_numbers(numbers):
    a, b = numbers
    result = add_numbers(a, b)
    assert result == 35


@pytest.fixture
def numbers():
    print("\nFixture: সংখ্যা pair তৈরি হচ্ছে (5, 10)")
    return 10,25  

def test_add_two_numbers(numbers):
    a, b = numbers
    result = add_numbers(a, b)
    assert result == 35

@pytest.fixture
def username():
    return "TAMIM"

def test_getting_message(username):
    result = format_greeting(username)
    assert   "TAMIM" in result
    assert result == "Hello TAMIM"



@pytest.fixture
def empty_list():
    return []

def test_add_item_to_list(empty_list):
    new_list = add_item_to_list(empty_list, 10)
    assert len(new_list) ==1



@pytest.fixture
def user_info_dict():
    """ডিকশনারি টেস্টিং-এর জন্য ডেটা সরবরাহ করে।"""
    return {"name": "Bob", "age": 30}
def test_get_user_name(user_info_dict):
    """get_user_info ফাংশন দিয়ে নাম বের করে টেস্ট করে।"""
    name = get_user_info(user_info_dict, "name")
    assert name == "Bob"


@pytest.fixture
def temp_file_with_content(tmp_path):
    """ফাইল টেস্টিং-এর জন্য একটি অস্থায়ী ফাইল তৈরি করে।"""
    file_path = tmp_path / "data.txt"
    with open(file_path, "w") as f:
        f.write("Test data for Pytest")
    yield file_path
    os.remove(file_path)




def test_file_reading(temp_file_with_content):
    """read_file_content ফাংশন টেস্ট করে।"""
    content = read_file_content(temp_file_with_content)
    assert "Test data for Pytest" in content





# এটি একটি Fixture ছাড়া কোড diye File Open 

import os
import pytest

def create_and_read_file(file_path):
    with open(file_path, 'w') as f:
        f.write("test content")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    os.remove(file_path) # প্রতিবার ম্যানুয়ালি ফাইল মুছতে হচ্ছে
    return content

def test_read_file():
    content = create_and_read_file("my_temp_file.txt")
    assert "test content" in content
#এই কোডটি যদি কোনো কারণে assert লাইনে ব্যর্থ হয়, তাহলে os.remove() লাইনটি রান করবে না এবং ফাইলটি মুছে যাবে না।


# এটি একই কাজ Fixture ব্যবহার করে
import pytest
import os

@pytest.fixture
def temp_file_path(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w") as f:
        f.write("test content")
    yield file_path
    os.remove(file_path) # এই অংশটি নিশ্চিতভাবে রান হবে, টেস্ট সফল হোক বা ব্যর্থ

def test_read_file_with_fixture(temp_file_path):
    with open(temp_file_path, 'r') as f:
        content = f.read()
    assert "test content" in content
    #fixture কেন ব্যবহার করবে তার ব্যাখ্যা নিচে দেওয়া হলো:


# এটি একটি Fixture ছাড়া কোড
import os
import pytest

def create_and_read_file(file_path):
    with open(file_path, 'w') as f:
        f.write("test content")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    os.remove(file_path) # প্রতিবার ম্যানুয়ালি ফাইল মুছতে হচ্ছে
    return content

def test_read_file():
    content = create_and_read_file("my_temp_file.txt")
    assert "test content" in content
#এই কোডটি যদি কোনো কারণে assert লাইনে ব্যর্থ হয়, তাহলে os.remove() লাইনটি রান করবে না এবং ফাইলটি মুছে যাবে না।




# এটি একই কাজ Fixture ব্যবহার করে
import pytest
import os

@pytest.fixture
def temp_file_path(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w") as f:
        f.write("test content")
    yield file_path
    os.remove(file_path) # এই অংশটি নিশ্চিতভাবে রান হবে, টেস্ট সফল হোক বা ব্যর্থ

def test_read_file_with_fixture(temp_file_path):
    with open(temp_file_path, 'r') as f:
        content = f.read()
    assert "test content" in content
#এই কোডে yield-এর পর os.remove(file_path) থাকায়, এটি নিশ্চিত করে যে ফাইলটি সবসময় মুছে যাবে। এটিই Fixture-এর একটি বড় সুবিধা। Fixture ব্যবহার করলে তোমার টেস্টিং কোড আরও নিরাপদ এবং কার্যকর হয়।






#Practise

@pytest.fixture
def file_read():
    file_path = file_handle("test.txt")
    with open(file_path, "w") as f:
        f.write("hello")
        yield file_path
        os.remove(f)

def test_file_handle(file_read):
    with open(file_read, "r") as f:
        content = f.read()
        assert "hello" in content
