# reduce（func，lst），其中func每次极端的结果继续和序列的每一个元素做累计计算。
# 注意：reduce（）传入的参数func必须接受两个参数
# 需求：把每次放入列表的结果累积和
import functools
list1 = [2, 3, 4, 5, 6]


def func(a, b):
    return a+b


result = functools.reduce(func, list1)
print(result)


