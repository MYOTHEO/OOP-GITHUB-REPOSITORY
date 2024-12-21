class Car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    

car = Car("Toyota","Black")
car1 = Car("Honda","Cyan")

print(f"Car:{car1.brand} Brand:{car1.color}")

car1.color = "Blue"

print(f"Car:{car.brand} Brand:{car1.color}")
print(f"Car:{car1.brand} Brand:{car1.color}")