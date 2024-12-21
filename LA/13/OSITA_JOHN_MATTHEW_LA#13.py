class Animal():
    def __init__(self, name, fishtype):
        self.name = name
        self.fishtype = fishtype
    
    def describeFish(self):
            print(f"Fishname: {self.name} \nType of fish: {self.fishtype} \nConfirmation: {self.can_swim}\n")
    
class Fish(Animal):
    def __init__(self, name, fishtype, can_swim):
        super().__init__(name, fishtype)
        self.can_swim = can_swim

miya = Fish("Miya","Sapsap", True)
miya.describeFish()
print(miya.can_swim)
