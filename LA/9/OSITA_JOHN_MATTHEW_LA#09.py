class Car:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return f"{self.brand}"
kotse = Car("Honda")
print(kotse)

del kotse
print(kotse)