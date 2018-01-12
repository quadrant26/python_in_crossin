list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = []

for i in list_1:
    if i % 2 == 0:
        list_2.append(i)

print(list_2)

list_3 = [i for i in list_1 if i % 2 == 0]
print(list_3)

list_4 = [i / 2 for i in list_1 if i % 2 == 0]
print(list_4)
