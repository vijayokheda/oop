class Car:
    def __int__(self, brand, model):
        self.brand = brand
        self.model = model
    

    def full_Name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are mean of transport"

    # @property      {(if sny csde we dont want to access code attribute so we can use the this method)}
    @property  
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"  

my_tesla = ElectricCar("tesla", "model S", "85kwh")
# print(my_tesla.model)
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())


# my_Car = Car("toyota", "corolla")
# print(my_Car.brand)
# print(my_Car.model)
# print(my_Car.full_Name())


# Multipl inheritance

class Battery:
    def bettery_info(self):
        return "this is battery"

class Engine:
    def enine_info(self):
        return "this is engine"

class ElectricCarTwo("Battery", "Engine", "Car"):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())