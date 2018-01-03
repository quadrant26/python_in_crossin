for i in range(0, 5):
    print('*')

for i in range(0, 5):
    print('*', end='')
    # print '*',   # python2 的写法

print('----------------------------------------------------')
for i in range(0, 5):
    for j in range(0, i+1):
        # print(i, j)
        print('*', end="")
    print()
