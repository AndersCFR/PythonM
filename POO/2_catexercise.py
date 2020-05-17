#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('michu',2)
cat2 = Cat('miau',4)
cat3 = Cat('mimi',5)


# 2 Create a function that finds the oldest cat
def oldest_one(*args):
    return(max(args))

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'The oldest cat is {oldest_one(cat1.age, cat2.age, cat3.age)} years old.')
