# else 表示如果没有异常执行的代码
try:
    print(33)
except Exception as result:
    print(result)

else:
    print('我是else，我是没有指定异常时执行的代码')
# try:
#     print(1 == 3)
# except Exception as a:
#     print(a)  # False
