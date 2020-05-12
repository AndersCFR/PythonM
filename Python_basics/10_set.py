#Set
#a data structure that gives us only uniques elements
#we dont have indexes with sets
my_set = {1,2,3,4,5,5}
my_set.add(100)
my_set.add(2)
print(my_set)

#example: return the list without duplicates
my_list = [1,2,3,4,5,5,5]
print(set(my_list))

print(1 in my_set)
print(len(my_set))
new_set = my_set.copy()  #coping
print(my_set.clear()) #clearing

#Methods
set1 = {100,500,661,2222,1,2,3,4,5,6}
set2 = {100,1,2,3,4,5,6,8}
print(set1.difference(set2)) #difference
print(set1.discard(5)) #discard or delete
print(set1)
print(my_set.difference_update(set1)) #set difference
print(set1.intersection(set2)) #intersection  it is equivalent  print(my_set & set1)
print(set1.isdisjoint(set2)) #is disjoint?
print(my_set.union(set1)) #it is equivalent  print(my_set | set1)

print(my_set.issubset(set1))  #subset
print(set1.issuperset(my_set))  #superset

