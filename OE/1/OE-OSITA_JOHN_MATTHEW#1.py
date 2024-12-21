class hero():
    def __init__ (self, name, role, dmg_type):  #parameter
        self.name = name #arguments
        self.role = role
        self.dmg_type = dmg_type
        
    def __str__(self):
        return "This is character object"
        
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"


hero_mm1 = hero("WANWAN", "marksman", "attack speed")
hero_fighter1 = hero("YU ZHONG", "fighter", "physical damage")
hero_tank1 = hero("TIGREAL", "tank", "physical damage")
hero_assassin1 = hero("GUSION", "assassin", "magical damage")
hero_mage1 = hero("GORD", "mage", "magical damage")

print(f'''
-----------------{hero_mm1.name}-----------------
{hero_mm1.role}
{hero_mm1.dmg_type}
{hero_mm1.describe()}

-----------------{hero_fighter1.name}-----------------
{hero_fighter1.role}
{hero_fighter1.dmg_type}
{hero_fighter1.describe()}

-----------------{hero_tank1.name}-----------------
{hero_tank1.role}
{hero_tank1.dmg_type}
{hero_tank1.describe()}

-----------------{hero_assassin1.name}-----------------
{hero_assassin1.role}
{hero_assassin1.dmg_type}
{hero_assassin1.describe()}

-----------------{hero_mage1.name}-----------------
{hero_mage1.role}
{hero_mage1.dmg_type}
{hero_mage1.describe()}
''')