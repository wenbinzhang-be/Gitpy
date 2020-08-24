# filter(func,lst)函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象，如果要转化为列表，可以用list（）来转换。
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1定义功能函数：过滤序列中的函数
def func(x):
    return x % 2 == 0


# 2调用filter
result = filter(func, list1)

print(result)  # #<filter object at 0x0000022F23E5EB08>

print(list(result))