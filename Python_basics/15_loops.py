# for

for item in [1,2,3,4,5,6]:
    for x in ['a', 'b', 'c']:
        print(item, x)

print('hi')

#iterable --> list, dictionary, tuple, set, string

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)


for item in user.keys():
    print(item)

for key, value in user.items():
    print(key, value)

# cpunt the items in a list
my_list = [1,2,3,4,5,6,7,8,9]
counter = 0
for item in my_list:
    counter = counter + 1
print(counter)

#range

print(range(2,100))
for number in range(0,100):
    print(number, 'just a number')

for it in range(0,10,2):
    print(it)

print('----------')
for www in range(10,0,-2):
    print(www)

print('----------')
for it in range(2):
    print(list(range(10)))

# enumerate
print('----------')
for i,char in enumerate('Helooo'):
    print(i, char)

print('-----------')
for i,char in enumerate((4,5,6,7,8)):
    print(i, char)

print('The index of video')
for i, char in enumerate(list(range(100))):
    if char==50:
        print(f'index of 50 is: {i}')


# While

i = 50
while 0<50:
    print(i)
    break

print('---------')
y = 0
while y < 50:
    print(y)
    pass
    y += 1
else:   #it only executes when the while doesnt have a break
    print('done ')

# iteration with for and while
print('----------')
my_list = [1,2,3]


i=0
while i < len(my_list):
    print(my_list[i])
    i += 1


while True:
    print('hello')
    pass    #it only goes to the next line
    response = input('say something: ')
    if response == 'bye':
        print('hello friend')
    break

for item in my_list:
    print(item)
    continue #it makes that back to loop without using the next liness
    print('helloo')
    
