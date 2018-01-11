# tuple
position = (1, 2)
geeks = ('Sheldon', 'Leonard', 'Rajesh', 'Howard')

print(position[0])
for g in geeks:
    print(g)

print(geeks[1:3])

def get_pos(n):
    return (n/2, n*2)

x,y = get_pos(6)
print(x)
print(y)

pos = get_pos(8)
print(pos)
