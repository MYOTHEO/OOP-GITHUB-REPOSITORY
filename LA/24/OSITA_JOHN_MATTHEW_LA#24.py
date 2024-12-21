#abstraction
from abc import ABC, abstractmethod
class GameCharacter(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name
    @abstractmethod
    def special_move(self):
        pass
class Warrior(GameCharacter):
    def special_move(self, move):
        print(f"{self.name} use the special move {move}")
class Mage(GameCharacter):
    def special_move(self, move):
        print(f"{self.name} use the special move {move}")
class Archer(GameCharacter):
    def special_move(self, move):
        print(f"{self.name} use the special move {move}")
class Healer(GameCharacter):
    def special_move(self, move):
         print(f"{self.name} use the special move {move}")

gc = Warrior("Warrior")
gc.special_move("Swings sword!")
gc = Mage("Mage")
gc.special_move("Casts a fireball!")
gc = Archer("Archer")
gc.special_move("Shoots an arrow!")
gc = Healer("Healer")
gc.special_move("Casts a healing spell on ally!")
