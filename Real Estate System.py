from abc import ABC, abstractmethod

class Property(ABC):
    @abstractmethod
    def display_details(self):
        pass

class ResidentialProperty(Property):
    def __init__(self, address, price, bedrooms, bathrooms):
        self.address = address
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def display_details(self):
        print(f"Residential Property: {self.address}, Price: ${self.price}, Bedrooms: {self.bedrooms}, Bathrooms: {self.bathrooms}")

class CommercialProperty(Property):
    def __init__(self, address, price, square_feet, parking_space):
        self.address = address
        self.price = price
        self.square_feet = square_feet
        self.parking_space = parking_space

    def display_details(self):
        print(f"Commercial Property: {self.address}, Price: ${self.price}, Square Feet: {self.square_feet}, Parking Space: {self.parking_space}")

class RealEstateAgent(ABC):
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    @abstractmethod
    def manage_property_listings(self):
        pass

    @abstractmethod
    def manage_client_information(self):
        pass

class ConcreteRealEstateAgent(RealEstateAgent):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)
        self.property_listings = []
        self.client_information = []

    def manage_property_listings(self):
        print(f"{self.name} is managing property listings.")

    def manage_client_information(self):
        print(f"{self.name} is managing client information.")


class Client:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def search_and_purchase_property(self, property):
        print(f"{self.name} is searching for properties.")
        property.display_details()
        print(f"{self.name} is purchasing the property.")


if __name__ == '__main__':
    
    residential_property = ResidentialProperty("999 Back St", 250000, 3, 2)
    commercial_property = CommercialProperty("754 Lck St", 500000, 2000, 10)

    agent = ConcreteRealEstateAgent("Bobik", "579-1468")
    client = Client("Alina", "111-5678")

    agent.manage_property_listings()
    agent.manage_client_information()

    client.search_and_purchase_property(residential_property)
    client.search_and_purchase_property(commercial_property)
