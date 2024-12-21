class BirthdayParty:
    def __init__(self, party_theme, list_of_foods, special_dish, secret_dish):
        self.party_theme = party_theme
        self.list_of_foods = list_of_foods
        self.special_dish = special_dish
        self.__secret_dish = secret_dish

    def print_foods(self):
        print(f"Party Theme: {self.party_theme}")
        print("Foods available:")
        for food in self.list_of_foods:
            print(f"- {food}")
        print(f"Special Dish: {self.special_dish}")
        self.__print_secret_dish()  

    def __print_secret_dish(self):
        print(f"(Secret Dish: {self.__secret_dish})")

party1 = BirthdayParty("Anime", ["Pizza", "Burgers", "Fries"], "Chocolate Cake", "Ice Cream")
party2 = BirthdayParty("Beach", ["Sandwiches", "Vegetable Salad", "Fruit Punch"], "Buko Salad", "Macarons")
party3 = BirthdayParty("Sports", ["Hot Dogs", "Nachos", "Popcorn"], "Cheesecake", "Brownie Sundae")

party1.print_foods()
print("\n")
party2.print_foods()
print("\n")
party3.print_foods()

