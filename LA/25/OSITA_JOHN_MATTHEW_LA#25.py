from abc import ABC, abstractmethod

class Character(ABC):
    @property #abstract property
    @abstractmethod
    def alias(self):
        pass

class Batman(Character):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property #abstract property
    def alias(self):
        return f"{self.__alias}"

paniki = Batman("Bruce Wayne", "Batman")
print(paniki.alias)

'''
print("Hello World"()) # This an Error
'''
