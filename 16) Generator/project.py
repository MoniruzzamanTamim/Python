import random
import os
import time
import json
from pprint import pprint

first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"]

# store_data = {} # এই গ্লোবাল ভেরিয়েবলটি Generator পাইপলাইনের জন্য প্রয়োজন নেই,
                  # তবে যদি আপনি প্রসেস করা সমস্ত ডেটা মেমরিতে রাখতে চান, তবে পরে ব্যবহার করতে পারেন।


class StudentInfo:
    def __init__(self, data_range, file_path):
        self.data_range = data_range
        self.file_path = file_path
    
    def dummy_data_generate(self):
        """
        একটি বড় ডামি ডেটা ফাইল তৈরি করে।
        কমা সেপারেটেড ফরম্যাটে প্রতিটি লাইনে ডেটা লেখে।
        """
        print(f"Creating '{self.file_path}' with {self.data_range} records...")
        try:
            # ফাইলটি লুপের বাইরে একবার 'w' মোডে ওপেন করুন
            with open(self.file_path, "w", encoding='utf-8') as sent_data:
                for i in range(self.data_range):
                    id = i + 1
                    name = random.choice(first_names)     
                    age = random.randint(18, 90)
                    city = random.choice(cities)
                    phone = f"01{random.randint(3,9)}{random.randint(100,999)}{random.randint(10000,99999)}"
                    # কমা এবং মানের মধ্যে কোনো অতিরিক্ত স্পেস নেই, যাতে পার্সিং সহজ হয়
                    sent_data.write(f"{id},{name},{age},{city},{phone}\n")
            print(f"Successfully created '{self.file_path}'.")
        except IOError as e:
            print(f"Error writing to file {self.file_path}: {e}")
            exit() # ফাইল তৈরি করতে না পারলে এক্সিট

    def read_large_file(self):
        """
        একটি বড় ফাইল থেকে লাইন-বাই-লাইন ডেটা পড়ে এবং Generator হিসেবে yield করে।
        মেমরি সাশ্রয়ী।
        """
        print(f"Reading data from '{self.file_path}'...")
        try:
            with open(self.file_path, "r", encoding='utf-8') as received_data:
                for data_line in received_data:
                    yield data_line.strip() # অতিরিক্ত whitespace (যেমন newline) সরান
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            exit()
        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")
            exit()
    
    @staticmethod
    def parse_data(lines_generator): # store_data আর্গুমেন্টটি সরানো হয়েছে
        """
        কাঁচা টেক্সট লাইন পার্স করে ডিকশনারি অবজেক্ট yield করে।
        """
        for item_line in lines_generator:
            try:
                parts = item_line.split(",")
                # প্রতিটি অংশ থেকে অতিরিক্ত স্পেস সরান
                id = int(parts[0].strip())
                name = parts[1].strip()
                age = int(parts[2].strip())
                address = parts[3].strip() # 'city' কে 'address' হিসেবে রিনেম করা হয়েছে
                phone = int(parts[4].strip())
                
                data = {
                    "id": id,
                    "name": name,
                    "age": age,
                    "city": address, # পূর্বে 'address' ছিল, এখন 'city'
                    "phone": phone
                }
                yield data # প্রতিটি পার্স করা রেকর্ড yield করুন
            except (ValueError, IndexError) as e:
                print(f"Skipping malformed line due to parsing error: '{item_line}' - {e}")
            except Exception as e:
                print(f"An unexpected error occurred during parsing line '{item_line}': {e}")
        
    @staticmethod
    def filter_by_age(parsed_data_generator, min_age, max_age):
        """
        বয়সের রেঞ্জ অনুসারে ডেটা ফিল্টার করে এবং ফিল্টার করা ডিকশনারি yield করে।
        """
        print(f"Filtering data for age between {min_age} and {max_age}...")
        for data_record in parsed_data_generator:
            # 'age' কী আছে কিনা তা পরীক্ষা করুন
            age = data_record.get("age")
            if age is not None and min_age <= age <= max_age: # সঠিক ফিল্টারিং লজিক
                yield data_record
    
    @staticmethod
    def add_category(filtered_data_generator):
        """
        ফিল্টার করা ডেটাতে বয়সের ভিত্তিতে একটি 'category' ফিল্ড যোগ করে।
        """
        print("Adding age categories...")
        for data_record in filtered_data_generator:
            age = data_record.get("age")
            if age is not None:
                if 18 <= age < 30: # ইনক্লুসিভ রেঞ্জ
                    data_record["category"] = "Young Adult"
                elif 30 <= age < 50:
                    data_record["category"] = "Adult"
                elif 50 <= age <= 90: # ইনক্লুসিভ রেঞ্জ
                    data_record["category"] = "Senior"
                else:
                    data_record["category"] = "Other" # 18 এর নিচে বা 90 এর উপরে
            yield data_record # পরিবর্তিত ডেটা রেকর্ড yield করুন


def main():
    # --- সমস্ত প্যারামিটার এখানে হার্ডকোডেড (Hardcoded Parameters) ---
    file_path ="16) Generator\\project.txt"  # ডেটা ফাইলের নাম
    num_records = 1000      # ফাইল তৈরি করার সময় রেকর্ডের সংখ্যা (যদি ফাইল না থাকে)
    min_filter_age = 20        # বয়সের সর্বনিম্ন সীমা (ফিল্টারের জন্য)
    max_filter_age = 70        # বয়সের সর্বোচ্চ সীমা (ফিল্টারের জন্য)
    # --- হার্ডকোডেড প্যারামিটার শেষ ---

    # StudentInfo ক্লাস ইনস্ট্যান্স তৈরি করা
    student_processor = StudentInfo(num_records, file_path)

    # ডেটা ফাইল তৈরি করা (যদি না থাকে)
    if not os.path.exists(file_path):
        student_processor.dummy_data_generate()
    else:
        print(f"Using existing data file: '{file_path}'.")

    start_time = time.time()

    # --- ডেটা পাইপলাইন তৈরি ---
    # ১. ফাইল থেকে লাইন পড়া (Generator)
    lines_generator = student_processor.read_large_file()

    # ২. লাইন পার্স করে ডিকশনারিতে রূপান্তর (Generator)
    # parse_data এখন একটি স্ট্যাটিকমেথড, তাই ক্লাস থেকে সরাসরি কল করুন
    parsed_data_gen = StudentInfo.parse_data(lines_generator)

    # ৩. বয়সের ভিত্তিতে ডেটা ফিল্টার করা (Generator)
    # filter_by_age এখন একটি স্ট্যাটিকমেথড
    filtered_data_gen = StudentInfo.filter_by_age(parsed_data_gen, min_filter_age, max_filter_age)

    # ৪. ক্যাটাগরি যোগ করা (Generator) - এটি ঐচ্ছিক ট্রান্সফরমেশন
    # add_category এখন একটি স্ট্যাটিকমেথড
    processed_data_gen = StudentInfo.add_category(filtered_data_gen)

    # ডেটা কনজিউম করা এবং রিপোর্ট তৈরি করা
    total_filtered_records = 0
    total_filtered_age = 0
    city_counts = {}
    category_counts = {}

    print("\n--- Processing Data and Generating Report ---")
    for record in processed_data_gen: # পাইপলাইনের শেষ Generator থেকে ডেটা নিন
        total_filtered_records += 1
        total_filtered_age += record.get('age', 0)

        city = record.get('city')
        if city:
            city_counts[city] = city_counts.get(city, 0) + 1
        
        category = record.get('category')
        if category:
            category_counts[category] = category_counts.get(category, 0) + 1

        # চাইলে প্রতিটি রেকর্ড এখানে প্রিন্ট করতে পারেন (ছোট ডেটাসেটের জন্য)
        # pprint(record) 

    end_time = time.time()
    
    print("\n--- Report Summary ---")
    print(f"Total filtered records: {total_filtered_records}")
    if total_filtered_records > 0:
        average_age = total_filtered_age / total_filtered_records
        print(f"Average age of filtered records: {average_age:.2f}")
    else:
        print("No records found matching the filter criteria.")
    
    print("\nRecords by City:")
    if city_counts:
        # শহর অনুযায়ী ডেটা সাজিয়ে প্রিন্ট করুন
        for city, count in sorted(city_counts.items(), key=lambda item: item[1], reverse=True):
            print(f"- {city}: {count}")
    else:
        print("No city data available for filtered records.")

    print("\nRecords by Category:")
    if category_counts:
        # ক্যাটাগরি অনুযায়ী ডেটা সাজিয়ে প্রিন্ট করুন
        for category, count in sorted(category_counts.items()):
            print(f"- {category}: {count}")
    else:
        print("No category data available for filtered records.")


    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds.")
    print("Memory efficiency: Generators process data line by line, avoiding loading the entire file into RAM.")


if __name__ == "__main__":
    main()
    