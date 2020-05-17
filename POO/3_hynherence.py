
class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        
    def attack(self):
        print(f'attacking with arrows you have of {self.arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin',100)

print(wizard1.sign_in())
wizard1.attack()
archer1.attack()
wizard1.sign_in()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))


