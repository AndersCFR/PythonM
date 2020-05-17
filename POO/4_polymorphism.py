
class User(object):
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in')
    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        
    def attack(self):
        print(f'attacking with arrows you have of {self.arrows}')


wizard1 = Wizard('Merlin', 50, 'merlin@outlook.com')
archer1 = Archer('Robin',100)
user1 = User('aa@p')

def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

print(user1.attack())
print(wizard1.email)


#Instrocpection
print(dir(wizard1))  #we have the complete information of access



