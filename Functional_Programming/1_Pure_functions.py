# Pure functions
# It always give us the same result
#It gives an output, it doesn't modify external data
# In functional programing we separate data and funtions

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return (new_list)

print(multiply_by2([1,2,3,4]))



# When we use func progra we have: map, filter, zip and reduce

#map: gives us the chance to not calling the func and evit create list inside the func
# it creates a map object, we can convert it in a list
def multiply_by3(item):
    return item*3

print(list(map(multiply_by3,[1,2,3])))

#filter

def only_odd(item):
    return item%2 != 0

print(list(filter(only_odd, [1,5,9,8,10])))  # it filters only the odd numbers

#zip

my_list = [1,2,3]
your_list = [10,20,30]

print(list(zip(my_list, your_list)))   # it zip the items together, it can mix iterables, ex: list with tuple


#reduce: it only returns a single value

from functools import reduce

def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))



