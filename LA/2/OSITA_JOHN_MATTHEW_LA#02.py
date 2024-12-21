class character:
    def __init__(self, name, role, damage):
        self.name = name
        self.role = role
        self.damage = damage
        
mlbb = character('Yu Zhong', 'Fighter', '300')
mlbb2 = character('Atlas', 'Tank', '180')
print(mlbb.name, mlbb.role, mlbb.damage, mlbb2.name, mlbb2.role, mlbb2.damage)