
from abc import ABC, abstractmethod

class Dish(ABC):
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    @abstractmethod
    def display(self):
        pass
    
    
    
class Appetizer(Dish):
    def display(self):
        return f"{self.name} (Appetizer) - ${self.price:.2f}"
    
class Entree(Dish):
    def display(self):
        return f"{self.name} (Entree) - ${self.price:.2f}"
    

class Menu(ABC):
    def __init__(self):
        self.dishes = []
        
    def add_dish(self,dish):
        self.dishes.append(dish)
        
    def display_menu(self):
        for dish in self.dishes:
            print(dish.display())
            
    
class Order:
    def __init__(self,customer,dishes):
        self.customer = customer
        self.dishes = dishes
        self.total_price = sum(dish.price for dish in dishes)
        
    def display_order(self):
        print(f"Order for {self.customer.name}:")
        for dish in self.dishes:
            print(f" - {dish.name} (${dish.price:.2f})")
        print(f"Total Price: ${self.total_price:.2f}")
        

class Customer:
    def __init__(self,name,contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []
        
    def place_order(self,menu,dish_names):
        ordered_dishes = [dish for dish in menu.dishes if dish.name in dish_names]
        if not ordered_dishes:
            print('Invalid Dish Name.')
            return
        
        new_order = Order(self,ordered_dishes)
        self.order_history.append(new_order)
        print('Order placed succesfully!')
        
    def view_order_history(self):
        if not self.order_history:
            print('No order history available.')
            return
        
        print(f'Order History for {self.name}:')
        for order in self.order_history:
            order.display_order()
            

if __name__ == '__main__':
    appetizer_menu = Menu()
    appetizer_menu.add_dish(Appetizer('All Cheese',12.00))
    appetizer_menu.add_dish(Appetizer('Сaviar', 30.00))
    
    entree_menu = Menu()
    entree_menu.add_dish(Entree('Breakfast Buck Burrito (BBB)',3.00))
    entree_menu.add_dish(Entree('Truffle Madeleine',250.00))
    
    
    Arnold = Customer('Arnold Hambardzumyan', 'arnold@mail.ru')
    

    print('\nAppetizer Menu')
    appetizer_menu.display_menu()
    print('\nEntree Menu')
    entree_menu.display_menu()
    
    print('\n')
    
    Arnold.place_order(entree_menu, ['Truffle Madeleine'])
    
    print('\n')
    
    Arnold.view_order_history()