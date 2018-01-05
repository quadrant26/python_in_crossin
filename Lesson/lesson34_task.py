from random import randint

print('Guess I want think!')
computer = randint(1, 100)

while True:
    print('Press you number')
    num = int(input())

    if num < 0:
        print('Exit...')
        break;

    if num > computer:
        print('Too big...')
    elif num < computer:
        print('Too small')
    elif num == computer:
        print('Cool')
        break
    
