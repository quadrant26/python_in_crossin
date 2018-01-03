from random import randint
print('Guess what I think?')
num = randint(1, 100)
bingo = False
while bingo == False:
    answer = int(input())

    if answer < num:
        print('too small!')

    if answer > num:
        print('too big!');

    if answer == num:
        print('BINGO, you are right!')
        bingo = True
