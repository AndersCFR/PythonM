#Lists
li = [1,2,3,4,5]
li2 = ['a','b','c','d']
li3 = [1,2,'a', True]

# List slicing    -not inmutability
cart = ['notebook','sunglass','book','toys','grapes']
print(cart[0:3])    #slicing in an interval
print(cart[0::2])  #giving a salt

cart[4] = 'laptop'
print(cart)
new_cart = cart[0:3]  #when we slice we create a new list, the values dont change
cart[1] = 'cool sunglases'
print(cart)
print(new_cart)
 
#   ---  List Methods
basket = [1,2,3,4,5]
print(len(basket)) 

#adding
print(basket.append(100))  #change the list, this method dont create a new list
print(basket)
#insert
basket.insert(4,200)
print(basket)
# extend
basket.extend([10000,20000,30000])
print(basket)

#removing
basket.pop()
print(basket)   #delete the last element of the list
basket.pop(0) #using an index
print(basket)

basket.remove(200) # we give the element that we want to remove
print(basket)

#more methods
print(basket.index(2))  
print(basket.index(2, 0, 4))  #look for an element with a range of indexes

#in
print('a' in 'anderson')
print(basket.count(2))

lista = ['a','c','b','e']
lista.sort()  #method
print(lista)
print(sorted(lista)) #function that produces a new array, dont modifie the list

#coping an list
basket2 = basket[:]
basket3 = basket.copy()
basket2.reverse()
print(basket2)
 
#len
print(len(basket2))
print(basket[::-1]) #when we slice we create a new list, in this case we reverse

#list with range  
print(list(range(100)))

#putting something between elements of a list
sentence = ' '
new_sentence =sentence.join(['hi','my','name','is','JOJO'])
print(new_sentence)

#in other way
new_sentence2 =' '.join(['hi','my','name','is','JOJO'])
print(new_sentence2)

#list unpacking

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)



