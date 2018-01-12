def func(x):
    print("'x' in the beginning of func(x):" , x)
    x = 2
    print("'x' in the end of func(x):" , x)

x = 50
func(x)
print("'x' after calling func(x):", x)


def func2():
    global y
    print('"y" in the begnning of func2(y): ', y)
    y = 2
    print("'y in the end of func2(y): '", y)

y = 50
func2()
print("'y' after calling func(y)", y)
