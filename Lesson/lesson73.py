from functools import reduce

lst = range(1, 101)
def add(x, y):
    return x + y

print( reduce(add, lst) )
print( reduce(lambda x, y: x + y, lst) )
