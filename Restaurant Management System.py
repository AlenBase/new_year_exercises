from abc import ABC, abstractmethod

class MenuItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def display(self):
        print(f"{self.name} - ${self.price}")

class Appetizer(MenuItem):
    def __init__(self, name, price, ingredients, portion_size):
        super().__init__(name, price, ingredients)
        self.portion_size = portion_size

    def display(self):
        super().display()
        print(f"Portion Size: {self.portion_size}")

class Entree(MenuItem):
    def __init__(self, name, price, ingredients, spice_level):
        super().__init__(name, price, ingredients)
        self.spice_level = spice_level

    def display(self):
        super().display()
        print(f"Spice Level: {self.spice_level}")

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def display(self):
        print(f"Customer: {self.name}, Contact: {self.contact_info}")

class Order(ABC):
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.total_price = sum(item.price for item in items)

    @abstractmethod
    def display(self):
        pass

class RegularOrder(Order):
    def display(self):
        print("Regular Order:")
        self.customer.display()
        for item in self.items:
            item.display()
        print(f"Total Price: ${self.total_price}")

class Review:
    def __init__(self, customer, rating, comments):
        self.customer = customer
        self.rating = rating
        self.comments = comments

    def display(self):
        print(f"Rating: {self.rating}/5, Comments: {self.comments}")

class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []
        self.reviews = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def display_menu(self):
        print("Menu:")
        for item in self.menu:
            item.display()

    def place_order(self, customer, items):
        order = RegularOrder(customer, items)
        self.orders.append(order)
        return order

    def view_order_history(self, customer):
        print(f"Order History for {customer.name}:")
        for order in self.orders:
            if order.customer == customer:
                order.display()

    def leave_review(self, customer, rating, comments):
        review = Review(customer, rating, comments)
        self.reviews.append(review)
        return review


appetizer1 = Appetizer("Spring Rolls", 5.99, ["Cabbage", "Carrot", "Pork"], "Small")
entree1 = Entree("Chicken Curry", 12.99, ["Chicken", "Potatoes", "Curry Sauce"], "Medium")

customer1 = Customer("Chechen", "chechen@mail.ru")

restaurant = Restaurant()

restaurant.add_menu_item(appetizer1)
restaurant.add_menu_item(entree1)

restaurant.display_menu()

order1 = restaurant.place_order(customer1, [appetizer1, entree1])

restaurant.view_order_history(customer1)

review1 = restaurant.leave_review(customer1, 4, "Great food!")

review1.display()
