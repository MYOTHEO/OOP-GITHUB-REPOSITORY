class Appliance:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
        
    def operate(self):
        print("Operating!")
    
    def info(self):
        print(f"Brand: {self.brand}\nModel:{self.model}")
        
class WashingMachine(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Washing clothes!")
    
class Refrigirator(Appliance):    
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Keeping food cold!")
        
class Microwave(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Heating food!")
    
washingMachine = WashingMachine("LG", "PT1200R\n")
refrigirator = Refrigirator("Condura","CBC283RI\n")
microwave = Microwave("Panasonic","Panasonic Genius Inverter SN67HS\n")

for appliances in [washingMachine, refrigirator, microwave]:
    appliances.operate()
    appliances.info()