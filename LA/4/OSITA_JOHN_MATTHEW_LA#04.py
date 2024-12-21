class character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return "Layla is a Marksman Hero"
    
    def describe(self, course):
        print(f"Si {self.name} ay {self.age} taong gulang na sa {course}.")
        
student = character('Meynard', 19)
print(student)