num = 10
print('Guess what i think?')
answer = int(input())
while answer != num:
    if answer < num:
        print('too small!')
    if answer > num:
        print('too big')
    answer = int(input())
print('guess is equal!')

