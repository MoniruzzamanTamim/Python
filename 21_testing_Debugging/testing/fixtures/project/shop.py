# shop.py

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """কার্টে একটি আইটেম যোগ করে।"""
        self.items.append(item)

    def remove_item(self, item_name):
        """নাম ব্যবহার করে কার্ট থেকে একটি আইটেম সরায়।"""
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)
                return True
        return False

    def get_total(self):
        """কার্টের সব আইটেমের মোট দাম হিসাব করে।"""
        total = sum(item['price'] for item in self.items)
        return total

# tamim = Carts()
# item = {"name":"tamim", "price":25}
# tamim.add_item(item)
# print(tamim.remove_item("tamim"))
# print(tamim.total_price())
        