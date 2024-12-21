class Spiderman:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def describeSpiderman(self):
        print(f"Spiderman: {self.name.upper()}\nAge:{self.age}")
    
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
        
class Andrew(Spiderman):    
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
        
class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
    
maguire = Tobey("Tobey Maguire", 49, "Spider-Man\n")
garfield = Andrew("Andrew Garfield", 41, "The Amazing Spider-Man\n")
holland = Tom("Tom Holland", 28, "Spider-Man: No Way Home\n")


print(maguire.name.upper())
print(maguire.movieTitle.upper())

print(garfield.name.upper())
print(garfield.movieTitle.upper())

print(holland.name.upper())
print(holland.movieTitle.upper())
