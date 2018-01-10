from random import randint

name = input("请输入你的名字：")

f = open('game.txt')
lines = f.readlines()
scores = {}
for i in lines:
    s = i.split()
    scores[s[0]] = s[1:]
f.close();

print(scores)
score = scores.get(name)
if score is None:
    score = [0, 0, 0]

game_times = int(score[0])      # 总游戏轮数
min_times = int(score[1])       # 最快猜出的轮数
total_times = int(score[2])     # 猜过的总轮数

# 计算平均轮数
if game_times >0:
    avg_times = float(total_times)/game_times
else:
    avg_times = 0

print('%s 已经玩了 %d 次， 最少 %d 轮猜出答案， 平均 %.2f 轮猜出答案' % (name, game_times, min_times, avg_times))

num = randint(1, 100)
print('Guess what i think?')
bingo = False
times = 0

while bingo == False:
    times += 1
    answer = int(input("请输入您的数字："))
    if answer < num:
        print("Too small!")

    if answer > num:
        print('Too big')
    if answer == num:
        print('Bingo')
        bingo = True

# 如果是第一次玩，或者本次的轮数比最小轮数还少，就记录本次成绩为最小轮数
if game_times == 0 or times < min_times:
    min_times = times

total_times += times    # 总游戏轮数增加
game_times += 1         # 游戏次数增加

scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''

for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line

f = open('game.txt', 'w')
f.write(result)
f.close()





















