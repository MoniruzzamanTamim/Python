# FOR IN LOOP - Syntax
# for val in sequence:
#     # run this code

# Example with range (looping 1 to 99, printing 50 each time)
for i in range(1, 100):
    print(50)

# ✅ List: Loop through vegetables
vegetables = [
    "Potato", "Tomato", "Carrot", "Cabbage", "Spinach",
    "Cauliflower", "Brinjal", "Onion", "Garlic", "Pumpkin"
]

# Print all vegetable names in UPPERCASE
for vegetable in vegetables:
    print(vegetable.upper())

# Check if all names contain only alphabets
for vegetable in vegetables:
    print(vegetable.isalpha())

# ✅ Loop with another List
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# ✅ Loop with String (not a list of strings)
name = "moniruzzaman"
for ch in name:
    print(ch.upper())

# ✅ Loop with Tuple
t = ("Tamim", 20)
for item in t:
    print(item)

# ✅ Loop with List OF  Tuple
students = [("Tamim", 90), ("Rohim", 85)]
for name, mark in students:
    print(f"{name} got {mark}")


# ✅ Loop with Dictionary
student = {
    "name": "Tamim",
    "age": 20,
    "grade": "A"
}

# Show only values (optional)
for key in student:
    print("KEY  Only:", key)
# Show only values (optional)
for value in student.values():
    print("Value Only:", value)

# Show key and value pairs
for key, value in student.items():
    print(key, ":", value)
