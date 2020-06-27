my_file = open("test.txt",'r')
print(my_file.read())
my_file.seek(0)

print(my_file.read())
my_file.seek(0)

print('-----see the diference-----')
print(my_file.readline())
my_file.seek(0)
print('-----see the diference-----')
print(my_file.readlines())
my_file.close()
