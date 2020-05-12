#Dictionary

dictionary = {
    'a': 1,
    'b': 5,
    'c': 'heloooo',
    'd': True,
    'e': [1,2,3,4,5,6]
}

print(dictionary['b'])
print(dictionary)

mylist = [
    {
    'a': 1,
    'b': 5,
    'c': 'heloooo',
    'd': True,
    'e': [1,2,3,4,5,6]
    },
    {
    'a': [99999,888,777,66],
    'b': 54    
    }
]

print(mylist[1]['a'][2]) #taking values from a dictionary

#the keys of the dictionaries have to be inmutable always and should be descriptible and unique
dict3 = {
    123:[1,2,3],
    True: 'hello',
    'ass': True
}

print(dict3[123])

#dictionary methods
user = {
    'age': 15,
    'name': 'Ander',
    'greeting': 'Heloo'
}
print(user.get('secondname')) #i get none if it doesnt exists
print(user.get('secondname',55)) #if dont exist use a default value

#creating a list
user2 = dict(name='Jhon')
print(user2)

print('hello' in user) #check if there is in the dictinary
print('age' in user.keys()) #check only in the keys
print('Ander' in user.values()) #check in the values

print(user.items()) #showing the keys and values

user2.clear() #deleting the elements
print(user2)

user3 = user.copy() #coping a full dictionary

print(user.pop('greeting')) #delete with the key
print(user)
print(user.popitem()) #random deletion of an item
print(user)
print(user.update({'age':21}))  #update an elemnt, but we can use to intrduce a vlue too
print(user)
print(user.update({'agesss':25}))
print(user)


