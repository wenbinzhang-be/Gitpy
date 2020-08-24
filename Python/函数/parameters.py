# 函数的参数：
# 默认参数、可选参数、关键字参数
# 参数概念:函数为了实现某项特定的功能，进而为了得到实现功能所需要的数据，参数就是为了得到外部数据的
# # 1必选参数
# def sum(a,b):#形式参数：只是意义上的一种参数，相当于一个标记，在定义的时候不占用内存地址。
#     sum=a+b
#     print(sum)
#     pass
# #函数的调用 在调用的时候必选参数必须要赋值
# sum(1,9)#1,9就是实际参数，简称实参，实实在在的参数，实际占用内存地址的。这个就叫必选参数
# # sum()#不允许这样调用，即不给实参
# #2：默认参数（缺省参数）始终存在参数列表中的尾部
# def sum1(a=20,b=30):
#     print('默认参数使用=%d'%(a+b))
#     pass
# sum1(10)#在调用的时候如果未赋值，就会用定义函数时给定的默认值
#3.可变参数（当参数的个数不确定时使用，比较灵活）
# def getcomputer(*args):#可变长参数
#     '''
#     计算累计和
#     :param args: 可变长的参数类型
#     :return:每次循环的结果累加
#     '''
#     # print(args)
#     result=0
#     for item in args:
#         result+=item
#         pass
#     print('result=%d' % result)
#     pass
# getcomputer(1,2)
# getcomputer(1,2,3)
# getcomputer(12,34,345,42)
# 4.关键字可变参数
# ** 来定义
# 在函数体内 参数关键字是一个字典类型 key是一个字符串
# # def keyFunc(**kwargs):
#     print(kwargs)
#     pass
# # keyFunc(name='zhangwenbin',age='23')
# dictA={'name':'张燕','age':'24','university':'xatu' }
# keyFunc(**dictA)
# keyFunc()
#混合使用
def codeM(*args,**kwargs):
    '''
    可选参数一定要放到关键词可选参数之前
    可选参数接受的数据是一个元组类型
    关键字可选参数接受的数据是一个字典类型
    :param args:
    :param kwargs:
    :return:
    '''
    print(args)
    print(kwargs)
codeM(1,2,34,)
codeM(name='zwb')



