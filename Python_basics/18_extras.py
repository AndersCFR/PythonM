# clean code

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(50))

# *args **kwargs this give us the chnace to have defined functions


def super_func(args):
    return print(args)


super_func('ooo')


def super_func2(*args):
    return sum(args)


print(super_func2(1, 2, 3, 4, 5))


def super_func3(*args, **kwargs):
    print(kwargs)
    print(args)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func3(1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs


def highest_even(li):
    envens = []
    for item in li:
        if item % 2 == 0:
            envens.append(item)
    return max(envens)


print(highest_even([1, 3, 50, 62]))

print('---------------')

# Scope
a = 1


def confusion():
    a = 5
    return a


print(a)
print(confusion())

# global, acumulating function with global
print('---------------')

total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())

# Crazy scope: nonlocal
print('---------')


def outer():
    x = "local"

    def inner():
        nonlocal x    # this modifies the value of the variable in the memory
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)


outer()

# 1 - start with local
# 2 - Parent local?
# 3 - global
# 4 - built in python functions
