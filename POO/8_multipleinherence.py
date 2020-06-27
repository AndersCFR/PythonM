
class User(object):
    def sign_in(self):
        print('logged in')
    def attack(self):
        pass


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        
    def checkarrow(self):
        print(f'number of arrows you have {self.arrows}')


# giving muktiple inherence
class Hybrid(Wizard,Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self,name, arrows)

hb1 = Hybrid('Borgie',50, 100)
print(hb1.checkarrow())
print(hb1.attack())
print(hb1.sign_in())



