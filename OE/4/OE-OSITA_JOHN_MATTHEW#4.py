class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, target):
        damage = self.power
        target.defend(self)
        print(f"{self.name} attacks {target.name} for {damage} damage. {target.name}'s health is now {target.health}.")
    
    def defend(self, attacker):
        self.health -= attacker.power
    

class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.is_special_move_active = False

    def special_move(self):
        print(f"{self.name} uses Shield Assult! Attack power doubled for the next attack.")
        self.is_special_move_active = True

    def attack(self, target):
        if self.is_special_move_active:
            original_power = self.power
            self.power *= 2
            super().attack(target)
            self.power = original_power 
            self.is_special_move_active = False
        else:
            super().attack(target)

class Mage(Character):
    def special_move(self):
        print(f"{self.name} casts Black Shoes!")
        return 100

    def attack(self, target):
        special_damage = self.special_move()
        target.health -= special_damage
        print(f"{self.name}'s Black Shoes does {special_damage} damage to {target.name}. {target.name}'s health is now {target.health}.")

class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Mountain Shocker! The attack ignores the target's defense.")
    
    def attack(self, target):
        special_damage = self.power 
        self.special_move()
        target.health -= special_damage
        print(f"{self.name}'s Mountain Shocker does {special_damage} damage to {target.name}. {target.name}'s health is now {target.health}.")

class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50
        print(f"{self.name}'s health is now {self.health}.")
    
    def attack(self, target):
        super().attack(target)


warrior = Warrior("Minsitthar", 2000, 200)
mage = Mage("Lylia", 1500, 150)
archer = Archer("Yi-Sun-Shin", 1200, 250)
monster = Monster("Balmond", 3000, 300)


warrior.attack(monster)
warrior.special_move()
warrior.attack(monster)

mage.attack(monster)

archer.attack(monster)


monster.attack(warrior)
monster.special_move()

monster.attack(mage)
monster.attack(archer)

characters = [warrior, mage, archer, monster]
for character in characters:
    character.special_move() 