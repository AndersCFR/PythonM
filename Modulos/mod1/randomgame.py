import sys
from random import randint

sys.argv

answer = randint(int(sys.argv[1]),int(sys.argv[2]))

while True:
    try:
        guess = int(input('guess a number 1~10:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('you win :(')
                break
        else:
            print('hey bozo, i said 1~10')
    except ValueError:
        print('please enter a number')
        continue
