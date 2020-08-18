# a=1 # 是不可变类型（int，str）
# def func(x):
#     print('x的地址:{}'.format(id(x)))
#     x=2
#     print('x修改了之后的地址:{}'.format(id(x)))
#     print(x)
#     pass
# # 调用函数
# print('a的地址:{}'.format(id(a)))
# func(a)
# print(a)

# 可变类型
li=[]
def testRenc(parms):

    li.append([1,2,3,4,5,0,6,7,8])
    print(id(parms))
    print('内部的{}'.format(parms))
    pass
print(id(li))
testRenc(li)
print('外部的变量对象{}'.format(li))
# 小结
# 1.在Python中，万物皆对象，在函数调用的时候，实参传递的就是对象的引用
# 2.了解了原理之后，就可以更好地去把控，在函数内部的处理是否会影响到函数外部的数据变化
# 参数传递是通过对象引用来完成，他传递的不是值，而是一个对象


