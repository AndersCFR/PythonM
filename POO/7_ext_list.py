#Extended list

class SuperList(list):  #list is the parent class
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))

super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
