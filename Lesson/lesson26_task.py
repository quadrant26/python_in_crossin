# 足球游戏 射门和电脑扑救
from random import randint, choice

print("Choose on side to shoot")
side = [1, 2, 3, 4, 6, 7, 8, 9]
print(side);

you = int(input());
print("You kicked %d" % you)

computer = randint(1, 10);
print('computer saved %d' % computer)
if computer == 5:
    computer = randint(1, 10);

if you != computer:
    print('Goal!')
else:
    print('Oops..')
