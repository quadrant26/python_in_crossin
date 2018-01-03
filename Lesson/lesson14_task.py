from random import randint

print('Guess what i think!')
num = randint(1, 100)
bingo = False

while bingo == False:
    answer = int(input())

    if answer < num:
        print('%d is too small!' % answer)

    if answer > num:
        print('%d is to big!' % answer)

    if answer == num:
        print('%d is equal!' % answer)
        bingo = True
