from collections import Counter,defaultdict, OrderedDict
import datetime
from array import array

li = [1,2,3,4,5,6,7,7,7]
print(Counter(li))    #creates a dict with the values
sentence = 'blah blah blah thinking in python'
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist',{
    'a': 1,
    'b': 2
})
print(dictionary['a'])
print(dictionary['d']) #it gives a defaut value with a callable object

d = OrderedDict()
d['a']=1
d['b']=2

d2 = OrderedDict()
d2['b']=2
d2['a']=1

print(d == d2) # it is false because dont have the same order of insertion

#**** since Python 3.7 we have ordred dict by default


print(datetime.time(5,45,2)) # creates a date object
print(datetime.date.today())
#in the performance(generatos) we use time

#***if we need array we can import them
arr = array('i',[1,2,3])  #we use types of c
print(arr[0])


