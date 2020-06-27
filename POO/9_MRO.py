# MRO - Method Resolution Order
#It is an algorithm that gives the order of execution with class and inherence
# http://www.srikanthtechnologies.com/blog/python/mro.aspx

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num)
print(D.mro())

print('------------------')

