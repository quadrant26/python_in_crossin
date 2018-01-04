from random import randint, choice

score_you = 0
score_computer = 0

computerside = [1, 2, 3, 4, 6, 7, 8, 9]
for i in range(5):
    print("-----Round %d -- you Kick!------" % (i+1))
    print("choose one side to shoot:")
    print("1,2, 3, 4, 6, 7, 8, 9")
    you = int(input())  # 输入你的方向
    computer = choice(computerside) # 电脑选择方向
    print("The computer choose side is %d" % computer )
    if you != computer: # 你进球了
        print("You shoot in, Cool!")
        score_you += 1
    else: # 电脑珠子了
        print("Computer save....")

    print("-----Round %d -- you Save!------" % (i+1))
    print("You save side:")
    print("1,2, 3, 4, 6, 7, 8, 9")
    you = int(input())  # 输入你的方向
    computer = choice(computerside) # 电脑选择方向
    print("The computer choose side is %d" % computer )
    if you == computer: # 你进球了
        print("You save, Cool!")
    else: # 电脑珠子了
        print("Computer get in....")
        score_computer += 1
        
    print("Score: %d(you) -- %d(computer)" % (score_you, score_computer))
