import utility
import shopping.shop



#other ways of import packages
from shopping.shop import buy
print(buy('chess'))

#multiply imports
from utility import multiply, divide

print(__name__)

if __name__ == '__main__':
    print('please run this')
    print(divide(5,2))
    
    print(utility.multiply(2,3))
    print(shopping.shop.buy('apple'))

