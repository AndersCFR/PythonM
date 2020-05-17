#OOP
#everything in python is an object

class BigObject:    #class
    pass

obj1 = BigObject()  #instanciate


class PlayerCharacter:
    membership = True
    def __init__(self, name='anonymous', age=18):   #Predefined values
        if( PlayerCharacter.membership and age>=18):
            self._name = name    #When we underscode we shouldnt touch
            self._age = age

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')
    
    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')
    
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1*num2




player1 = PlayerCharacter('Cindy',18)
player2 = PlayerCharacter()

print(player1)
print(player1.name)
print(player1.age)
print(player1.run())
print(player1.shout())

print(player2.shout())

print(player1.adding_things(2,3))
print(player1.adding_things2(2,3))

player1.speak()

