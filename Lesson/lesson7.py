thisIsLove = input()
if thisIsLove:
    print("再转生就该勇敢留下来")

num  = 10
print("Guess what i think?")
answer = int(input())
if answer < num:
    print("too small!")
if answer > num:
    print('too big!')
if answer == num:
    print('BINGO')
