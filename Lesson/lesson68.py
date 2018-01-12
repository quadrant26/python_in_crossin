def func(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

func(1, 3, 5, 6, 7, 8, 9)

def printAll(*args):
    for i in args:
        print(i)

printAll(1, 2, 3)
printAll(3, 2, 1)
