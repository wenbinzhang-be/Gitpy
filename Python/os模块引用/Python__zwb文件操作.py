# 面向对象的概念： 文件操作的作用就是把一些内容（数据）存储存放起来，可以让程序下一次执行的时候直接使用
# 而不必重新制作一份，省时省力。
# 2.1文件操作步骤
# 1.打开文件2，读写等操作3.关闭文件（相当于保存）如果不关闭，将会一直消耗计算机内存
# 2.1.1打开 在Python中，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件
# 1 打开 open（）
# f = open('test.txt','w')
# # 2读写操作write（） read（）
# f.write('ass')
# # 3 关闭 close()
# f.close()
# r:如果文件不存在，会报错,不支持写入操作
# f = open('word0.txt','r')
# f.close()
# w：如果文件不存在，会自动创建一个文件，支持写入操作，写入的信息会被下一次覆盖掉
# f = open('word1.txt','w')
# f.write('a123')
# f.close()
# a：如果文件不存在，会自动创建一个新的文件，支持写入，在原有文件的基础上追加文件
# f = open('word2.txt','a')
# f.write('wejij')
# f.close()
# 访问模式是否可以省略,可以省略，如果省略，则默认为访问模式为"r"
# f = open('123.txt')
# f.close()
# read() 格式： 文件对象.read(num),num表示要从文件中读取的字节，不写默认读全部。
# 底层有/n，换行符也占用一个字节
# f = open('test.txt','r')
# print(f.read())
# print(f.read(10))
# f.close()
# readlines() 可以按招行的方式把整个文件的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
# f = open('test.txt','r')
# con = f.readlines()#当我txt文件中有中文时，出现了错误，
# print(con)
# f.close()
'''
测试目标
1，r+，w+，a+.区别：
2.文件指针读数据读取的影响

'''
# r+:r 没有文件则报错；文件指针在开头，所以能读取出来数据
# f = open('test.txt','r+')
# con=f.read()
# print(con)
# f.close()
# w+: 没有文件回新建文件，w特点：文件指针在开头，用新内容覆盖旧内容
# f = open('test.txt','w+')
# con=f.read()
# print(con)
# f.close()
# a+: 没有文件会新建文件文件指针在结尾，无法读取数据（文件指针后面没有数据）
# f = open('word1.txt', 'a+')
# con = f.read()
# print(con)
# f.close()
# seek():作用：用来移动文件指针
"""
语法：文件对象.seek(偏移量，起始位置)0开头1，当前2结尾
面向对象的概念： 1.r访问时，改变文件指针位置改变读取数据开始位置或把文件指针放到结尾（无法读取数据）
      2.a 改变文件指针的位置，做到可以读取出来数据

"""
# # f=open('test.txt','r+')
# f=open('test.txt','a+')
# # 1.改变读取数据开始位置
# # f.seek(2,0)
#
# # f.seek(0,2)#(2,1)
# # 2. a改变文件指针位置，做到可以读取数据
# # f.seek(0,0)
# f.seek(0)
# con=f.read()
# print(con)
# f.close()
