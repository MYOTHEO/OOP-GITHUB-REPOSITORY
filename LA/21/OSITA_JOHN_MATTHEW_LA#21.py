class Manok:
    def __init__(self, chicken, breading, sauce, itlog, flour):
        self.__chicken = chicken #private
        self.breading = breading
        self.sauce = sauce
        self.itlog = itlog
        self.flour = flour
        
    def __str__(self):
        return f"My favorite food is Fried Chicken and the ingredients are: {self.__chicken}, {self.breading}, {self.sauce}, {self.itlog}, {self.flour}"

    def my_chicken(self): #getter method
        return self.__chicken
    def set_chicken(self, bagong_value): #setter method
        self.__chicken = bagong_value
    
friedChicken = Manok("Chicken", "Crispy Fry", "Mang Tomas", "egg", "flour")
friedChicken2 = Manok("Chicken", "Sky Flakes", "Ketchup", "egg", "flour")
friedChicken3 = Manok("Chicken", "Bread Crumbs", "Gravy", "egg", "flour")
friedChicken.set_chicken = ("limang Chicken")
print(friedChicken.set_chicken)