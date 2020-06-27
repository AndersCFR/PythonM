# Lambda expressions
# There are funtions that we use only once


from functools import reduce

my_list = [1,2,3,4]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item%2 != 0, my_list)))

print(reduce(lambda acc, item: acc+item, my_list))

# lamba expresion that squares a list
list1 = [52,99,23,45]

print(list(map(lambda item: item**2,list1)))


# lambda expresion that sorts a list of tuples based in the second number
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1])
print(a)



