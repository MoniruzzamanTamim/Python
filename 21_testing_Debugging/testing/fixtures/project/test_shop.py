# test_shop.py
import pytest
from shop import Cart

# --- Fixtures ---

@pytest.fixture
def empty_cart():
    """টেস্টের জন্য একটি খালি Cart অবজেক্ট তৈরি করে।"""
    return Cart()

@pytest.fixture
def product_items():
    """টেস্টের জন্য কিছু ডামি আইটেম সরবরাহ করে।"""
    return [
        {'name': 'apple', 'price': 1.50},
        {'name': 'banana', 'price': 0.75},
        {'name': 'orange', 'price': 1.20}
    ]

# --- Tests ---

def test_add_item_to_cart(empty_cart, product_items):
    """Fixture ব্যবহার করে কার্টে আইটেম যোগ করা টেস্ট করে।"""
    apple = product_items[0]
    empty_cart.add_item(apple)
    
    assert len(empty_cart.items) == 1
    assert empty_cart.items[0]['name'] == 'apple'

def test_remove_item_from_cart(empty_cart, product_items):
    """Fixture ব্যবহার করে কার্ট থেকে আইটেম সরানো টেস্ট করে।"""
    empty_cart.add_item(product_items[0]) # apple যোগ করা হলো
    empty_cart.add_item(product_items[1]) # banana যোগ করা হলো
    
    removed = empty_cart.remove_item('apple')
    
    assert removed is True
    assert len(empty_cart.items) == 1
    assert empty_cart.items[0]['name'] == 'banana'

def test_get_total_price(empty_cart, product_items):
    """Fixture ব্যবহার করে মোট দামের হিসাব টেস্ট করে।"""
    empty_cart.add_item(product_items[0]) # 1.50
    empty_cart.add_item(product_items[1]) # 0.75
    
    total_price = empty_cart.get_total()
    
    assert total_price == 2.25
    assert total_price != 2.50