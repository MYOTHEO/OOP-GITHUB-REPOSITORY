class Dog:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Bark!")
        
class Cat:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Meow!")
            
class Bird:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Chirp!")
        
class Fish:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("...")

dog = Dog("Bruno")
cat = Cat("Bruce")
bird = Bird("Bruddha")
fish = Fish("Brulee")

def animal_sounds(animal):
    animal.speak() 

for animal in [dog, cat, bird, fish]:
    animal_sounds(animal)
