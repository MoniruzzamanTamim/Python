

# #Check Add Function Work ...........................................
# from main_file import add 

# def test_add_positive_numbers():
#     assert add_numbers(2, 3) == 5

# def test_add_negative_numbers():
#     assert add_numbers(-2, -3) == -7


# #Test   Calculator Program ..............................................
# from main_file import Calculator
# cal = Calculator()
# def test_cal_add():
#     assert cal.add(10,10) == 20
#     assert cal.add(-10,-10) == -20 
#     assert cal.add(-10,-10) == -25 #Show an Error bcz -10 & -10 is -20 not -25
#     assert cal.add(-10,-10) == -20 


# def test_cal_minus(): 
#     assert cal.minus(10,5) == 5
#     assert cal.minus(5,10) ==-5
# def test_cal_multiply():
#     assert cal.multiply(10,10) == 100
# def test_cal_divide():
#     assert cal.divide(10,10) == 1




#Test DataType  ................................................................

# from main_file import string_test

# def test_string():
#     name_from_function = string_test()
#     assert type(name_from_function) is str
#     assert name_from_function == "Tamim"



# #Test Only Singel Test [pytest test_math.py::test_mul  # নির্দিষ্ট টেস্ট ফাইল ও ফাংশন]...........................................
# from main_file import string_test , number_test

# def test_string():
#     name_from_function = string_test()
#     assert type(name_from_function) is str
#     assert name_from_function == "Tamim"
# def test_number_s():
#     name_from_function = number_test()
#     assert type(name_from_function) is int

# #Singel Test Assign Korar jonno ===>  Command: python3 -m pytest  [Test-File]::[test_function] ==> python3 -m pytest  test_file.py::number_test -v



# # #Test Group / Tag Wise [ Use Decrator for seperate Group ]...........................................................................
# import pytest
# from main_file import string_test, number_test


# @pytest.mark.number
# def test_add_number():
#     assert 2 + 2 == 4 

# @pytest.mark.number
# def test_add_num():
#     assert 3 + 2 == 5 

# # -------------------
# # String group tests
# # -------------------
# @pytest.mark.strings
# def test_string():
#     name_from_function = string_test()
#     assert type(name_from_function) is str

# @pytest.mark.strings
# def test_string_value():
#     name_from_function = string_test()
#     assert name_from_function == "Tamim"


# # -------------------
# # Number  group tests
# # -------------------

# @pytest.mark.number
# def test_number_value():
#     number_from_fuction = number_test()
#     assert    number_from_fuction == 123456





# #Test Weather App ( API CAlling/File Open) using fixures ............................................
# import sys
# from pathlib import Path
# # weatherApp.py এর path যোগ করো
# sys.path.append(str(Path(__file__).resolve().parents[0] / "19_Web_APIs_and_HTTP"))
# from weatherApp import use_test_purpose

# def test_data_valid():
#     api_key = "5a68f249fd2cd34161ebdfb432ddd41f"
#     city = "dhaka"
#     assert use_test_purpose(city,api_key)
#     data,status = use_test_purpose(city, api_key, return_status=True)
    # assert status == 200




#OpenFile 
