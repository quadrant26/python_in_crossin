word = 'helloworld'

# 遍历
for c in word:
    print(c)

# 索引访问
print(word[0])
print(word[1])

# 切片
print(word[1:4])
print(word[2:])
print(word[:])
print(word[:-5])

# 连接
newword = ','.join(word)
print(newword);
