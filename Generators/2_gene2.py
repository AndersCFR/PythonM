# Range  will give us the numbers and never creates the list
# generators dont consume memory
# a list es iterable but not a generator

def generator_function(num):
    for i in range(num):
        yield i*2 #when we use yield we get an object, it is better than get only a value


for item in generator_function(100):
    print(item)

g = generator_function(100)
print(g)

next(g)
next(g)
next(g)
print(next(g))  #yield passes the funtion and return when it is called by next




