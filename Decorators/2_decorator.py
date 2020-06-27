#Decorator: overcharging funtions
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***********')
        func(*args, **kwargs)
        print('-----------------')
    return wrap_func

@my_decorator  #it is like take a func like a variable
def hello(greeting, emoji=':)'):
    print(greeting,emoji)

hello('hii')


@my_decorator
def bye():
    print('see you later')

bye()