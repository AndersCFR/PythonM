# Generator: permite crear secuencia de valores en el tiempo
print(range(100))
print(list(range(100)))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)



