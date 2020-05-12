#Tuples
#this data structure is inmutable, we cant sort
my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

#when we use dict.items() it shows a tuple, we can use a tuple as a key in dict

new_tuple = my_tuple[1:2] #slicing

x,y,z, *other = (6,7,8,9,10,11,12)
print(other)

#methods are only count and index
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

