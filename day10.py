 
"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

class Cart:
    def __init__(self):
        self.database = []

    def add_to_cart(self, product):
        self.database.append(product)
        print("Added to cart")

    def remove_from_cart(self, name):
        for product in self.database:
            if product.name == name:
                self.database.remove(product)
                print("Removed from cart")
                return
        print("Product not found")

    def display_cart(self):
        if not self.database:
            print("Cart is empty")
        else:
            print("Products in cart:")
            for product in self.database:
                product.display_info()

c = Cart()

while True:
    print("Options:")
    print("1. Add to cart")
    print("2. Remove from cart")
    print("3. Display details")
    print("4. Exit")
    choice = int(input())

    if choice == 1:
        print("Enter the name of the product:")
        name = input()
        print("Enter the price of the product:")
        price = float(input())
        print("Enter the quantity:")
        quantity = int(input())
        product = Product(name, price, quantity)
        c.add_to_cart(product)
    elif choice == 2:
        print("Enter the name of the product to remove:")
        name = input()
        c.remove_from_cart(name)
    elif choice == 3:
        c.display_cart()
    elif choice == 4:
        break
    else:
        print("Invalid choice")

"""


import unittest

class Dummy(unittest.TestCase):
    def test1(self):
        pass
    def test2(self):
        pass
if __name__=="__main__":
    unittest.main()