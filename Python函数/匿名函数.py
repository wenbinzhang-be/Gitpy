# 匿名函数就是没有名字的函数
# 语法：
# lambda 参数1、参数2、参数3：执行表达式
#特点：
# 使用lambda关键字去创建函数
# 没有名字
# 匿名函数冒号后面的表达式有且只有一个，注意：是表达式而不是语句
# 匿名函数自带了一个return，而return的结果就是表达式计算后的结果
#缺点
# lambda 只能是单个表达式，不是一个代码块，lambda 的设计就是为了满足简单函数的场景，
# 仅仅能封装有限的逻辑，复杂逻辑实现不了，必须使用def处理
# def computer(x,y):
#     '''
#     计算累加和
#     :param x:
#     :param y:
#     :return:
#     '''
#     return (x+y)
# # print(computer(10,23))
# # M=lambda x,y:x+y
# # print(M(23,19))
# #通过一个变量去调用匿名函数
# N=lambda a,b,c:a*b*c
# print(N(654,353,4532))
# ####################lambda 与三元运算##################
age=35
# print('可以参军'if age>18 else '继续上学')#可以替换传统双分支的写法

# Funtest=lambda x,y:x if x>y else y
# print(Funtest(23,45))
# rs=(lambda x,y:x if x>y else y)(16,12)#直接调用
# print(rs)
# re=(lambda x :(x**2)+80)(2)
# print(re)