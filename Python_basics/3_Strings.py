# STRINGS

print(type("hi Anderson 24/7 !"))
username = 'supercoder'
password = 'superscret'
# this is the way we can use a multiple line string
long_string ='''
        WOW
        O O

        ---
        |||
         _

        '''

print(long_string)

first_name= 'Anderson'
last_name='Cardenas'
full_name = first_name+' '+ last_name
print(full_name)

#String Concatenation

print('hello' + 'Anderson')

#Type conversion
print(type(int(str(199))))
a = str(100)
b = int(a)
c = type (b)
print(c)

# Escape Sequence
weather = '\t It\'s sunny "kind" of \'sunny\' \n \tHope you have a great day'
print(weather)

#formatted strings
name = 'Anderson'
age =  21
print('Hi ' + name + ' you are ' + str(age) + ' years old.')
print(f'hi {name}. You are {age} years old')  # This is a new feature of python 3
print('hi {}. You are {} years old'.format('Jhonny',str(55)))  # This is a new feature of python 3
print('hi {1}. You are {0} years old'.format(name,age))  # This is a new feature of python 3
print('hi {name2}. You are {age2} years old'.format(name2='Sally',age2=100))  # This is a new feat of python 3

#String indexes: python index te position of the letters [start:finish:stepover]

selfish = 'ma me mi mo mu'
print(selfish[0]) #position
print(selfish[2:5])  #[start:finish]
print(selfish[1:5:3])  #[start:finish:stepover]
print(selfish[5:]) #[start:end]
print(selfish[:5]) #[begin:end]
print(selfish[::1]) #[::strpover]
print(selfish[-5]) #begining by the end 
print(selfish[::-1]) #beginign by tehe end you can reverse

#Inmutability
statement = '0123456789' +'12'
print(statement) #we cant change the value of an inex of a string by inmutability



