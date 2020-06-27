import random
#this are libraries that we have installed in python

print(random)
print(dir(random))

print(random.random()) #random number between 0 and 1
print(random.randint(52,56)) 
print(random.choice([1,2,3,4,5,6]))
my_list = [1,2,3,4,5,6]
random.shuffle(my_list)
print(my_list)




