# map(func,lst),将传入的函数变量作用到lst变量的每个元素中，并将结果组成新的迭代器返回
# 需求1：计算list1序列中各个数字的2次方
def func(x):
    return x ** 2


list1 = [1, 2, 3, 4, 5]

result = map(func, list1)
print(result)  # <map object at 0x0000020828B2EA08>内存地址
print(list(result))
