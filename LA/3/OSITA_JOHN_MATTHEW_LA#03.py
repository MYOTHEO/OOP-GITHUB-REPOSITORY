class character:
    def __init__(self, name, role): #parameter
        self.name = name
        self.role = role #arguments
        
    def describe(self, damage):
        print(f"{self.name} is a {self.role} and has a damage which is {damage}.")
        
        
student = character('Nathan', 'Marksman')
student.describe(100)