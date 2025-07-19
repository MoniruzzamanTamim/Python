##Normal 
# try :
#     num = int(input("Type First Number: "))
#     num2= int(input("Type Second Number: "))
#     result = num/num2
#     print(result)
# except ValueError:
#     print("ValueError: " +"Please Write Int Type Data Only")
# except TypeError:
#     print("TypeError" +"Please Write Int Type Data Only")
# except ZeroDivisionError:
#     print("ZeroDivisionError:"+ "Zero Diye purno songkha vag kora zay na")
# except Exception as e:
#     print("Wrong: ",e)


# # পাইথন ইন্টারপ্রেটার বা একটি স্ক্রিপ্টে:
# print("বিল্ট-ইন এক্সেপশনগুলো (আংশিক তালিকা):")
# for name in dir(__builtins__):
#     obj = getattr(__builtins__, name)
#     if isinstance(obj, type) and issubclass(obj, Exception):
#         if obj is not Exception: # Exception বেস ক্লাসটি বাদ দিতে
#             print(f"- {name}")




