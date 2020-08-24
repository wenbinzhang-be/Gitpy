# 2.3.1 语法
# try:
#     可能发生的错误
# except:
#     如果捕获到该异常类型执行的代码
# try:
#     # print(num)
#     print(1/0)
# except NameError:
#     print('有错误')
# 注意：
# 1.如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
# 2.一般try下方只放一行尝试执行的代码。
# 2.3.3 部或多个指定异常
# 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式执行
# try:
#     print(1/0)
# except(NameError, ZeroDivisionError):
#     print('有错误')

# 2.3.4 捕获异常描述信息
# 为什么捕获异常描述信息？
# 异常类型： 异常描述信息（能辅助我们排查错误）
# try:
#     print(1/0)
# except (NameError, ZeroDivisionError)as result:  # rsult为变量存储异常信息
#     print(result)
# 2.3.5 捕获所有异常，不用指定具体的错误类型
try:
   崇文门
except Exception as result:
    print(result)
# 不会影响后续代码的执行
we = 1
print(we)  # 1
