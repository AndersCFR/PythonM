#Convertions

#My own solution 

name = 'Anders Cardenas'
age = 21
relationship_status = 'single'
birth_year =int(input('What year were you born?'))

age= 2020 - birth_year

print(f'Hi {name} you are {age}')

#Simple Password Checker
username = input("What is your user?")
password = input("What is your password")
hidden_pass = '*'*len(password)
print(f'{username} your password {hidden_pass} is {len(password)} letters long')


