from random import randint

f = open('game.txt')
score = f.read().split()
print(score)
f.close();


game_times = int(score[0])      # 总游戏轮数
min_times = int(score[1])       # 最快猜出的轮数
total_times = int(score[2])     # 猜过的总轮数

# 计算平均轮数
if game_times >0:
    avg_times = float(total_times)/game_times
else:
    avg_times = 0

print('你已经玩了 %d 次， 最少 %d 轮猜出答案， 平均 %.2f 轮猜出答案' % (game_times, min_times, avg_times))

num = randint(1, 100)
print('Guess what i think?')
bingo = False

while bingo == False:
    answer = int(input("请输入您的数字："))
    if answer < num:
        print("Too small!")

    if answer > num:
        print('Too big')
    if answer == num:
        print('Bingo')
        bingo = True
