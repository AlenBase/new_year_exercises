
from abc import ABC, abstractmethod

class Cars(ABC):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
    
    @abstractmethod
    def display_info(self):
        pass
    
        

class ElectricInterface(ABC):
    @abstractmethod
    def battery_range(self):
        pass


class HybridInterface(ABC):
    @abstractmethod
    def fuel_efficiency(self):
        pass
    
    
class ElectricCar(Cars, ElectricInterface):
    def __init__(self, make, model, price, battery_range):
        super().__init__(make, model, price)
        self.battery_range = battery_range
        
    def display_info(self):
        return f"{self.make} {self.model} (Electric) - Price: ${self.price}, Battery Range: {self.battery_range} miles"

    
    def battery_range(self):
        return self.battery_range


class HybridCar(Cars, HybridInterface):
    def __init__(self, make, model, price,fuel_efficiency):
        super().__init__(make, model, price)
        self.fuel_efficiency = fuel_efficiency
        
    def display_info(self):
        return  f"{self.make} {self.model} (Hybrid) - Price: ${self.price}, Fuel Efficiency: {self.fuel_efficiency} mpg"
    
    
    def fuel_efficiency(self):
        return self.fuel_efficiency
    
    
    
class Customers:
    def __init__(self,name,contact_information):
        self.name = name
        self.contact_information = contact_information
        

class Dealership:
    def __init__(self):
        self.car_inventory = []

    def add_car_to_inventory(self, car):
        self.car_inventory.append(car)
        print(f"{car.make} {car.model} added to inventory.")

    def remove_car_from_inventory(self, car):
        if car in self.car_inventory:
            self.car_inventory.remove(car)
            print(f"{car.make} {car.model} removed from inventory.")
        else:
            print(f"{car.make} {car.model} not found in inventory.")

    def display_inventory(self):
        for car in self.car_inventory:
            print(car.display_info())




class SalesOperation(ABC):
    @abstractmethod
    def make_sale(self,car,customer):
        pass
    
    @abstractmethod
    def view_sales_history(self):
        pass
    
    
class SalesPeople(SalesOperation):
    def __init__(self, name, comission_rate):
        self.name = name
        self.comission_rate = comission_rate
        self.sales_history = []
        
    def make_sale(self, car, customer):
        sale_amount = car.price
        comission = sale_amount * (self.comission_rate / 100)
        self.sales_history.append({"car":car, "customer":customer, "comission":comission})
        return f"Sale successful! {self.name} sold a {car.make} {car.model} to {customer.name} for ${sale_amount}. Commission earned: ${comission}"
    
    
    def view_sales_history(self):
        for sale in self.sales_history:
            car_info = sale['car'].display_info()
            customer_info = f"Customer: {sale['customer'].name}, Contact: {sale['customer'].contact_information}"
            comission_info = f"Commission: ${sale['comission']}"
            print(f"{car_info}\n{customer_info}\n{comission_info}\n{'='*30}")
            


def main():
    electric_car = ElectricCar('Volkswagen','ID4',35000, 300)
    hybrid_car = HybridCar('Toyota','Prius',23000, 50)
    
    dealership = Dealership()
    dealership.add_car_to_inventory(electric_car)
    dealership.add_car_to_inventory(hybrid_car)
    
    customer = Customers('Artur Hambardzumyan','123-456-7890')
    salesperson = SalesPeople('Irina', 7)
    
    print("\nAvailable Cars:")
    dealership.display_inventory()
    
    print("\nSales Transaction:")
    sale_result=salesperson.make_sale(electric_car,customer)
    print(sale_result)
    
    
    dealership.remove_car_from_inventory(electric_car)
    
    print("\nSales history:")
    salesperson.view_sales_history()
    
    print("\nAvailable Cars:")
    dealership.display_inventory()
    
if __name__ == '__main__':
    main()