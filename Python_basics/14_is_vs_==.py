# ==  vs is

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
print('1' == 1)

# is: compare with memory adress
print('---is------')
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])  #it is false because they are in different memory spaces
print('1' is 1)
a = [1,2,3]
b = [1,2,3]
print("--the best example--")
print( a is b)
print( a == b)
