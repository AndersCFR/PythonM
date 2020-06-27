# Error Handling
'''
We have: type errors
syntax error
nem error: undefined name used in code
zero divison
value error
building error

https://docs.python.org/3/library/exceptions.html

'''
while True:
    try:
        age = int(input('What is your age?'))
        2/age
       # raise Exception('hey cut it out') # it stops the program
    except ValueError:
        print('please enter a number')
        
    except ZeroDivisionError:
        print('please enter a number higher than zero')
    else:
        print('thank you')
        break
    finally:
        print('ok, I am finally done') # this line always appears