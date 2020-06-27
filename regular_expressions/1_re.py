import re

pattern = re.compile('this')
string = 'search this inside of this text please'
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d= pattern.match(string)
print(a)      
print(a.start())
print(a.end())
print(a.group()) # it only will give us the value
print(b)
print(c)
print(d)