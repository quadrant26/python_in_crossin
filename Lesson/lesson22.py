from random import randint

print('Guess what I think?')
num = randint(1, 100)
bingo = False

def isEqual(num1, num2):
    if num1 < num2:
        print("too small")
        return False
    if num1 > num2:
        print('too big')
        return False
    if num1 == num2:
        print('bingo')
        return True

while bingo == False:
    answer = int(input())
    bingo = isEqual(answer, num)
