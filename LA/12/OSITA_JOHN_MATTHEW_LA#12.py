class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def describeToy(self):
            print(f"Brand: {self.name} \nPrice: {self.price}")
    
class Marksman(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

cat = Marksman("Hot Wheels GruMobile","129")
cat.describeToy()