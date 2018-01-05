f1 = open("lesson3.py");
data = f1.read()

f2 = open('data.txt', 'a');
f2.write(data)

f1.close()
f2.close();


str2 = input('请输入内容:')
f3 = open('data.txt', 'w')
f3.write(str2)
f3.close();
