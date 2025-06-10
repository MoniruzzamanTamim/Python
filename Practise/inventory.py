import random
import json
import os
inventory = []

def add_product():
    id = int(input("Type Product ID: "))
    name = input("Type Product Name: ").capitalize()
    quantity = int(input("Type Product quantity: "))
    price = int(input("Type Product Price: "))

    product = {
        "id": id,
        "name": name,
        "quantity": quantity,
        "price": price
    }
    inventory.append(product)

def view_all():
    print("View All Products ............")
    # for serial in range(len(inventory)):
    #     print(serial+1)
    if not inventory:
        print("No products in inventory.")
    else:
        for serial, product in enumerate(inventory, start=1):
            print(f"{serial}) ID: {product['id']}, Name: {product['name']}, Quantity: {product['quantity']}, Price: {product['price']}")

def search_by_id():
    user_id= int(input("Serach By ID: "))
    filtered = [e for  e in inventory if e["id"] == user_id]
    if not filtered:
        print("This ID Not Available") 
        return
    for e in filtered:
         print(f" ID: {e['id']}, Name: {e['name']}, Quantity: {e['quantity']}, Price: {e['price']}")
    total_price = sum(e['price'] for e in filtered)
    total_quantity = sum(e['quantity'] for e in filtered)
    print(f" Total Quantity This ID: {total_quantity} & Total Price: {total_price}")

def update():
    user_id= int(input(" Type Product  ID: "))
    filtered = [e for  e in inventory if e["id"] == user_id]
    if not filtered:
        print("This ID Not Available") 
        return
    for e in filtered:
      print(f" ID: {e['id']}, Name: {e['name']}, Quantity: {e['quantity']}, Price: {e['price']}")
      while True:
        print("1) Update Product Price")
        print("2) Update Product Quantity")
        print("3) Exit")
        option = int(input("Choice your Option: "))
        if option == 1:
            upd_price = int(input("Update Product Price: "))
            e["price"]= upd_price
            print(f"AFTER UPDATE  Product Price:   ID: {e['id']}, Name: {e['name']}, Quantity: {e['quantity']}, Price: {e['price']}")
        elif option == 2:
            upd_quantity= int(input("Update Product quantity: "))
            e["quantity"]= upd_quantity
            print(f"AFTER UPDATE Product Quantity:    ID: {e['id']}, Name: {e['name']}, Quantity: {e['quantity']}, Price: {e['price']}")
        elif option == 3:
            break
            print("Thank You for Using My Apps")
        else:
          print("Please Choice 1 OR 2")


def remove():
     user_id= int(input(" Type Product  ID: "))
     filtered = [e for  e in inventory if e["id"] == user_id]
     if not filtered:
         print(f"No product found with ID {user_id}")
     for e in filtered:
         inventory.remove(e)
         print(f"Your Product(s) with ID {user_id} Deleted Successfully")

def save_load(filename = "inventory.json"):
    print("\n1. Save Data\n2. Load Data")
    option = int(input("Choise an Option: "))
    if option ==1:
        with open(filename, "w") as save:
            json.dump(inventory, save)
            print("Your Data Save Successfully....")
    elif option == 2:
        if os.path.exists(filename):
            with open(filename, "r") as load:
                load_data = json.load(load)
                print("Your Data Load Successfully....\n", )
                for e in load_data:
                    print(f"ID: {e['id']}, Name: {e['name']}, Quantity: {e['quantity']}, Price: {e['price']}")
           
        else:
            print("No File In Program .")
            
    else: 
        print("Choice Right Option")

def category():
    category = set()
    for e in inventory:
        word = e["name"].split()
        category.update(word)
    print("category: ", category)




def main():
    
    while True:
        print("\n1. Add Product\n2. View All Products\n3. Search By ID\n4. Update stock quantity or price\n5. Delete product\n6. Save/load product\n7. Unique Category\n8. Exit")
        option = int(input("Choose an Option: "))
        if option == 1:
            add_product()
        elif option == 2:
            view_all()
        elif option == 3:
           search_by_id()
        elif option == 4:
           update()
        elif option == 5:
           remove()
        elif option == 6:
           save_load()
        elif option == 7:
           category()
        elif option == 8:
            break
        else:
            print("Invalid Option")
main()
