from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    @abstractmethod
    def display_info(self):
        pass

class ElectronicsProduct(Product):
    def __init__(self, name, price, description, brand):
        super().__init__(name, price, description)
        self.brand = brand

    def display_info(self):
        return f"Electronics: {self.name} by {self.brand}, Price: ${self.price}"

class ClothingProduct(Product):
    def __init__(self, name, price, description, size):
        super().__init__(name, price, description)
        self.size = size

    def display_info(self):
        return f"Clothing: {self.name}, Size: {self.size}, Price: ${self.price}"

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.orders = []

    def purchase_product(self, product, quantity):
        order = Order(self, product, quantity)
        self.orders.append(order)
        return order

    def view_order_history(self):
        print(f"\nOrder History for {self.name}:")
        for order in self.orders:
            print(f"Order ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Total Price: ${order.total_price}")

    def leave_review(self, order, rating, feedback):
        if isinstance(order.product, ProductWithReviews):
            order.product.add_review(self, rating, feedback)
        else:
            print("Cannot leave a review for this product.")

class Order:
    order_counter = 0

    def __init__(self, customer, product, quantity):
        self.order_id = Order.order_counter + 1
        Order.order_counter += 1
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.total_price = quantity * product.price

class Review:
    def __init__(self, customer, rating, feedback):
        self.customer = customer
        self.rating = rating
        self.feedback = feedback

class ProductWithReviews(Product):
    def __init__(self, name, price, description):
        super().__init__(name, price, description)
        self.reviews = []

    def add_review(self, customer, rating, feedback):
        review = Review(customer, rating, feedback)
        self.reviews.append(review)

    def display_info(self):
        return f"{super().display_info()}\nDescription: {self.description}\nReviews: {len(self.reviews)}"

if __name__ == "__main__":
    laptop = ElectronicsProduct("Laptop", 1200, "Powerful laptop for professional use", "MSI")
    t_shirt = ClothingProduct("T-Shirt", 20, "Comfortable cotton t-shirt", "Large")

    customer = Customer("John Kluni", "john_kluni@yandex.com")

    order1 = customer.purchase_product(laptop, 1)
    order2 = customer.purchase_product(t_shirt, 5)

    customer.view_order_history()

    customer.leave_review(order1, 5, "Great laptop.")
    customer.leave_review(order2, 4, "Nice t-shirt.")

    print("\nProduct Information with Reviews:")
    print(laptop.display_info())
