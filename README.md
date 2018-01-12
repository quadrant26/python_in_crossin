# python_in_crossin
python study online

1. 字符串格式化

    %d

        num = 18
        print 'My age is %d' % num

    %f

        print ‘Price is %f’ % 4.99
        输出
        Price is 4.990000

        如果你想保留两位小数，需要在f前面加上条件：%.2f
        print ‘Price is %.2f’ % 4.99
        输出
        Price is 4.99]

    %s

        name = 'Crossin'
        print '%s is a good teacher.' % name
        输出
        Crossin is a good teacher.

2. 类型转化

    int(x) #把x转换成整数
    float(x) #把x转换成浮点数
    str(x) #把x转换成字符串
    bool(x) #把x转换成bool值

3. List

    I = [365, 'everyday', 0.618, True]

    1. 访问

        print(I[0])

    2. 修改

        I[0] = 123
        print(I[0])

    3. 添加

        I.append(1024)
        print(I)

    4. 删除

        del I[0]
        print(I)

    5. 切片 (slice)

        切片操作符是在[]内提供一对可选数字，用:分割。冒号前的数表示切片的开始位置，冒号后的数字表示切片到哪里结束。同样，计数从0开始。
        注意，开始位置包含在切片中，而结束位置不包括。

        如果不指定第一个数，切片就从列表第一个元素开始。
        如果不指定第二个数，就一直到最后一个元素结束。
        都不指定，则返回整个列表的一个拷贝。

    6. 连接 join()

        s = ';'
        li = ['apple', 'pear', 'orange']
        fruit = s.join(li)
        print fruit

        

4. 字符串

    1. 分割 split

        split默认是按照空白字符进行分割
        split("-") （- 指定的分割符号） 可以指定分割的符号

    2. 遍历

        for i in 'str':
            print(i);

    3. 索引访问

        'str'[0]

    4. 切片 slice

        print word[5:7]
        print word[:-5]
        print word[:]

    5. 连接 join()

        newword = ','.join(word)

5. 文件操作

    1. 读文件

        file() || open()

        py2里可以使用 open 或 file 方法打开文件，py3 只能使用 open。

        f = open('data.txt')
        data = f.read()
        print data
        f.close()

        readline() #读取一行内容
        readlines() #把内容按行读取至一个list中

    2. 写文件

        python默认是以只读模式打开文件。如果想要写入内容，在打开文件的时候需要指定打开模式为写入
        f = open('output.txt', 'w')

        'w'就是writing，以这种模式打开文件，原来文件中的内容会被你新写入的内容覆盖掉，如果文件不存在，会自动创建文件。
        
        不加参数时，open为你默认为'r'，reading，只读模式，文件必须存在，否则引发异常。

        另外还有一种模式是'a'，appending。它也是一种写入模式，但你写入的内容不会覆盖之前的内容，而是添加到文件中。

        f.write()
        f.writelines()

6. 字典 dict

    d = {key1 : value1, key2 : value2 }

    1. 键必须是唯一的；

    2. 键只能是简单对象，比如字符串、整数、浮点数、bool值。

    3. list就不能作为键，但是可以作为值。

    访问 

        d[key1]
    
    遍历

        for key in d:
            print(key + d[key])

    修改值 || 新建

        d[key] = new value

    删除

        del d[key]

    



7. 异常处理

        try:
            f = open('non-exist.txt')
            print('file opened!')
            f.close()
        except:
            print('file not exists')

        print('Done')

8. 模块

    import moduleName

    查看模块内的方法和变量

        dir(moduleName)

    只使用模块内的某一个方法或变量

        from math import pi
    
    为了便于理解和避免冲突，你还可以给引入的方法换个名字

        from math import pi as math_pi


9. 函数

    1. 默认参数
        
        函数有多个参数时，如果你想给部分参数提供默认参数，那么这些参数必须在参数的末尾

        def func(a, b=5):
            print(a+b)

        def print(name = 'world'):
            print('hello, ' + name)


10. 类

    1. 空的类

        class Person:
            pass

    2. 

        class Person:

            name = 'k'

            def sayHi(self):
                print('hello %s' % self.name)

    3. 参数

        class Person:
            def __init__(self, name):
                self.name = name
            
            def hello(self):
                print(self.name)

        name = Person('t')
        name.hello()

11. 元祖

    1. 基础 ( 元组中的元素在创建之后就不能被修改。 )

        tuple(1, 2)

    2. 使用

        def get_pos(n):
            return (n/2, n*2)

        # 1
        x, y = get_pos(50)
        print(x + " " + y)
        # 2
        pos = get_pos(50)
        print pos[0]
        print pos[1]

12. pickle

    1. 存储文件 ( python3 下 pickle 以 2 进制的格式存储和读取文件内容 )
        
        f = open('file', 'wb')
        pickle.dump(data, f)
        f.close()

    2. 读取文件

        f = open('file', 'rb')
        data = pickle.load(f)
        print(data)
        f.close()

13. 函数的参数传递

    1. 默认值

        def hell0(a=1, b=2):
            print(a, b)

    2. *args (tuple)

        def hello(*args):
            print(args) # tuple

    3. **kargs (dict)

        def hello(**kargs):
        print(kargs)

    tips

        在混合使用时，首先要注意函数的写法，必须遵守：
            带有默认值的形参(arg=)须在无默认值的形参(arg)之后；
            元组参数(*args)须在带有默认值的形参(arg=)之后；
            字典参数(**kargs)须在元组参数(*args)之后。
        
        调用时也需要遵守：
            指定参数名称的参数要在无指定参数名称的参数之后；
            不可以重复传递，即按顺序提供某参数之后，又指定名称传递。

        1.按顺序把无指定参数的实参赋值给形参；
        2.把指定参数名称(arg=v)的实参赋值给对应的形参；
        3.将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
        4.将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。

    4. lambda

        lambda 参数列表: 表达式

14 方法

    1. map

        map(function, list or tuple)

    2. reduce

        在Python 3里,reduce()函数已经被从全局名字空间里移除了,它现在被放置在fucntools模块里 用的话要 先引入：
        
        from functools import reduce 
        reduce(lambda x, y: x+y, list or tuple)

15. 多线程
    
    thread 

        start_new_thread(function, args[, kwargs])
            function 是开发者定义的线程函数，
            args 是传递给线程函数的参数，必须是tuple类型，
            kwargs 是可选参数。
