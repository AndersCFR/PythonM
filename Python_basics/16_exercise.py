# Exercise
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

'''#Display the image below to the right hand side where the 0 is going to be ' ', 
and the 1 is going to be '*'. This will reveal an image!
'''

for  item in picture:
    for x in item:
        if x == 0:
         print(' ',end='') 
        else:
         print('*',end ='')
    print('\n')

print('Happy Christmas')

# exercise 2 find duplicates
some_list = ['a','b','c','b','d','m','n','n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

