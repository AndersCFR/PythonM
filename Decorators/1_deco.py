def hello(func):
    func()

def greet():
    print('still here')

a = hello(greet)

print(a)

'''
 This features of python gives us the chance to have decorators.

High Order Function HOC: is a functio that accepts another functions
or return another function
'''
