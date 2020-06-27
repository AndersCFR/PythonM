# Comprenhension of list, set, dictionary


my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)


#Lists
#we can do the same 

my_list2 = [char for char in 'hello']
print(my_list2)

my_list3 = [num for num in range(0,100)]
print(my_list3)

my_list4 = [num*2 for num in range(0,100)]
print(my_list4)

my_list5 = [num**2 for num in range(0,100)] #squares
print(my_list5)

my_list6 = [num**2 for num in range(0,100) if num % 2 ==0] #squares onlu of even numbers
print(my_list6)

#Sets 

set1 = {char for char in 'hello'}
print(set1)

set2 = {num for num in range(0,100)}
print(set2)

set3 = {num*2 for num in range(0,100)}
print(set3)

set4 = {num**2 for num in range(0,100)} #square
print(set4)

set5 = {num**2 for num in range(0,100) if num % 2 ==0} #squares only of even numbers
print(set5)


#Dictionaries

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = { key:value**2 for key, value in simple_dict.items()}
my_dict2 = { key:value**2 for key, value in simple_dict.items() if value%2 ==0}
print(my_dict)
print(my_dict2)

#item is the key and the double is the values

my_dict3 = {num: num*2 for num in [1,2,3]}
print(my_dict3)

