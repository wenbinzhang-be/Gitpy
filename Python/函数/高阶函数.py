# # abs():求绝对值
# print(abs(-10))
# # round():四舍五入
# print(round(1.5))
#
# def add_sum(a,b):
#     return round(abs(a))+round(abs(b))
# print(add_sum(-1,2.6))

# 高阶函数写法,f是第二个参数，用来接收传入的函数
def sum_num(c,d,f):
    return f(c) + f(d)


result1 = sum_num(1.2, 2.2, abs)
print(result1)
result2 = sum_num(1.2, 1.2, round)
print(result2)