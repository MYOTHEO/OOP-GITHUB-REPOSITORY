class Manok:
    def __init__(self, chicken, breading, sauce, itlog, flour):
        self.chicken = chicken
        self.breading = breading
        self.sauce = sauce
        self.itlog = itlog
        self.flour = flour
        
    def __str__(self):
        return f"My favorite food is Fried Chicken and the ingredients are: {self.chicken}, {self.breading}, {self.sauce}, {self.itlog}, {self.flour}"

friedChicken = Manok("Chicken", "Crispy Fry", "Mang Tomas", "egg", "flour")
friedChicken2 = Manok("Chicken", "Sky Flakes", "Ketchup", "egg", "flour")
friedChicken3 = Manok("Chicken", "Bread Crumbs", "Gravy", "egg", "flour")

print(friedChicken)
print(friedChicken2)
print(friedChicken3)