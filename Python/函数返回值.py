# 函数返回值
# 概念：函数执行完以后会返回一个对象，如果函数的内部有return，就可以返回实际的值，否则为none
# 类型：可以反悔任意类型，返回值类型应该取决于return后面的类型
# 用途：给调用方返回数据
# 在一个函数体内可以出现多个return值，但是肯定只能返回一个return
# 如果一个函数体内执行了return，意味着函数就执行完成退出了，return后面的代码语句就不会执行
def sum(a,b):
    sum=a+b
    return sum
    pass
# we=sum(10,30)#将返回值赋给其他的变量
# print(we)#函数的返回值返回到调用的地方
# def calcomputer(num):
#     li=[]
#     result=0
#     i=1
#     while i<=num:
#         result+=i
#         pass
#         i+=1
#     li.append(result)
#     return li
#     pass
# #调用函数
# value=calcomputer(10)
# print(type(value))#value类型
# print(value)
def returnTuple():
    return {'name':'张文斌','age':'你多大了'}
    # return 1,2,3
ou=returnTuple()
print(type(ou))
print(ou)
