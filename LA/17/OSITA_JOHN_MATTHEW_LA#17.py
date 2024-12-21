class Player:
    def __init__(self, name, health, atk_power):
        self.name = name
        self.health = health
        self.atk_power = atk_power
    
    def attack(self, target):
        target.health = target.health - self.atk_power
        print(f"{chang_e.name}: HP:{chang_e.health}, ATK:{chang_e.atk_power}")
        print(f"{nana.name}: HP:{nana.health}, ATK:{nana.atk_power}")
    
    def heal(self, amount):
        amount.health = self.health + 1000
        print(f"{chang_e.name}: has restored HP:{amount.health}, ATK:{chang_e.atk_power}")
        print(f"{nana.name}: has restored HP:{amount.health}, ATK:{nana.atk_power}")
        
chang_e = Player("Chang_e", 1500, 300)
nana = Player("Nana", 1500, 300)


nana.attack(chang_e)
chang_e.attack(nana)
nana.attack(chang_e)
chang_e.attack(nana)
nana.attack(chang_e)
chang_e.attack(nana)
nana.attack(chang_e)
chang_e.attack(nana)
nana.attack(chang_e)
chang_e.attack(nana)

while True:
    if (chang_e.health <= 0):
        print("Nana Wins!")
        break
    elif (nana.health <= 0):
        print("Chang_e Wins!")
        break
    else:
        nana.heal(chang_e.health)
        chang_e.heal(nana.health)

#    