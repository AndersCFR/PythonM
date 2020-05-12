# Conditionals

is_old = False
is_license = True

if is_old and is_license:
    print('You are old enough to drive!')
elif is_license:
    print('You can drive')
else:
    print('you cant drive')

print('check check')

#Truthy and Falsey

old = bool('hello')
licensed = bool(5)
print(bool('hello'))
print(bool(5))
print(bool(''))
print(bool(0))
print(bool(None))

passw = 12345
user = 'Anderson'
if passw and user:
    print('all right baby')

is_friend = True
is_user = False
if is_friend or is_user:
    print('best friend for ever')


