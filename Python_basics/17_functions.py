# functions


def say_hello():
    print('heloooo')


def show_tree():
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]

    for item in picture:
        for x in item:
            if x == 0:
                print(' ', end='')
            else:
                print('*', end='')
        print('\n')

    print('Happy Christmas')


say_hello()
show_tree()

print('the memory direction of the function:', show_tree)


# Parameters and arguments

def say_name(name, lastname):
    print(f'hello {name} {lastname}')


say_name('Anderson', 'Cardenas')

# Positional Arguments
# Keyword arguments
say_name(name='Lionel', lastname='Messi')


# Default Parameters
def hello(phrase='good luck'):
    print(f'You are saying {phrase}')


hello()
hello('Hey broo')


# Return functions

def suma(n1, n2):
    return n1 + n2


print('Suma: ', suma(10, 5))
t = suma(2, 3)
print('Otra suma:', suma(t, 5))

'''
Methods vs Functions

---  'hello'.capitalize()

--list()
print()

'''


# Docstrings, lets check what happen over test

def test(a):
    '''
    Info: this function is so stupid
    '''
    print(a)


test('oooooo')
help(test)  # getting information
print(test.__doc__)  # getting information away
