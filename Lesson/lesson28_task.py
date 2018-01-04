from random import randint, choice

side = [1, 2, 3, 4, 6, 7, 8, 9];
score = [0, 0]

def kick():
    print("-------- you kicked! -------")
    print("choose one side to shoot !")
    print("from 1, 2, 3, 4, 6, 7, 8, 9 choose")
    you = int(input())
    print("You kicked %d !" % you);
    computer = choice(side)
    print("computer save %d " % computer)
    if you != computer:
        print("you kicked, Cool")
        score[0] += 1
    else:
        print("Computer is saved...")

    print("Score: %d(you) --- %d(computer)" % (score[0], score[1]))

    print("-------- you save! -------")
    print("You save one side!")
    print("from 1, 2, 3, 4, 6, 7, 8, 9 choose")
    you = int(input())
    print("You save %d !" % you);
    computer = choice(side)
    print("computer choose side is %d " % computer)
    if you == computer:
        print("you save the goal, Cool")
    else:
        print("Computer is shoot in...")
        score[1] += 1

    print("Score: %d(you) --- %d(computer)" % (score[0], score[1]))

for i in range(5):
    print("----------------------------------ROUND %d ------------------------------------" % (i+1))
    kick()

while( score[0] == score[1] ):
    i += 1
    print('=======  ROUND %d=========' % (i+1))
    kick()

if score[0] > score[1]:
    print("You Win.")
else:
    print("You Lose.")
