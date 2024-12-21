class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def describePhone(self):
            print(f"Your Brand: {self.brand} \nYour Model: {self.model}")
    
class Android(Phone):
    def __init__(self, name, model):
        Phone.__init__(self, name, model)

selpon = Android("POCO","X3 GT")
selpon.describePhone()