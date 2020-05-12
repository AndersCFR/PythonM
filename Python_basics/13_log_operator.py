#Logical operator

print(4>5)
print(5==5)
print('Anderson' == 'Anderson') #this is crazy, love python
print('a'>'A')
print(not(True))

#magician exercise

is_magician = False
is_expert = True

'''check if magician and expert: "you are a master magician" if magician but not expert "you are getting there
if you ar enot magician but you are expert "you need powers"'''

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("you are getting there")
elif not is_magician and is_expert:
    print("you need magic powers")


