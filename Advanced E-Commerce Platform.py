from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class ElectronicsProduct(Product):
    def __init__(self, name, price, description, brand):
        super().__init__(name, price, description)
        self.brand = brand

class ClothingProduct(Product):
    def __init__(self, name, price, description, size):
        super().__init__(name, price, description)
        self.size = size

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

class Order(ABC):
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    @abstractmethod
    def calculate_total_price(self):
        pass

class OnlineOrder(Order):
    def calculate_total_price(self):
        return sum(product.price for product in self.products)

class ECommercePlatform:
    def __init__(self):
        self.products = [
            ElectronicsProduct("Laptop", 1000, "Powerful laptop for work", "BrandX"),
            ClothingProduct("T-shirt", 20, "Comfortable cotton t-shirt", "Medium"),
        ]
        self.customers = []
        self.orders = []

    def search_products(self, keyword):
        return [product for product in self.products if keyword.lower() in product.name.lower()]

    def create_customer(self, name, contact_info):
        customer = Customer(name, contact_info)
        self.customers.append(customer)
        return customer

    def place_order(self, customer, selected_products):
        order = OnlineOrder(customer, selected_products)
        self.orders.append(order)
        return order

    def view_order_history(self, customer):
        return [order for order in self.orders if order.customer == customer]


if __name__=='__main__':
    ecommerce_platform = ECommercePlatform()

    search_results = ecommerce_platform.search_products("laptop")
    print("Search Results:")
    for product in search_results:
        print(f"{product.name} - ${product.price}")


    customer1 = ecommerce_platform.create_customer("Alex", "ale@gmail.com")

    selected_products = [product for product in ecommerce_platform.products if "laptop" in product.name.lower()]
    order1 = ecommerce_platform.place_order(customer1, selected_products)


    order_history = ecommerce_platform.view_order_history(customer1)
    print("\nOrder History:")
    for order in order_history:
        print(f"Order Total: ${order.calculate_total_price()}")

