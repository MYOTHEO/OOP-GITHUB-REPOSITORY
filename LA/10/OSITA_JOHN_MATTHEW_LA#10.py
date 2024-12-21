class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    def describeVehicle(self):
        print(f"Brand: {self.brand} \nModel: {self.model} \nFuel Type: {self.fuel_type}\n")

class Car(Vehicle):
    pass
class Motorcycle(Vehicle):
    pass
toyota = Car("Honda", "Civic", "gasoline")
toyota.describeVehicle()

toyota = Motorcycle("Mio", "Click", "gasolina")
toyota.describeVehicle()

