lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = []
for i in lst_1:
    lst_2.append(i * 2)

print(lst_2)

lst_21 = [ i*2 for i in lst_1 ]
print(lst_21)


def double_func(x):
    return x*2

lst_22 = map(double_func, lst_1)
print(list(lst_22))

lst_23 = map(lambda x: x*2, lst_1)
print(list(lst_23))


lst_1 = [1,2,3,4,5,6]

lst_2 = [1,3,5,7,9,11]

lst_3 = map(None, lst_1)

print( lst_3 )

lst_4 = map(None, lst_1, lst_2)

print( list(lst_4) )
