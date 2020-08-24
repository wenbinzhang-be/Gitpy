# finally 表示程序不管正确还是错误都要执行的代码，例如关闭文件。
# try:
#     print(1)
# except Exception as result:
#     print(result)
# finally:
#     print('我就是不管你错不错都要执行我的finally语句')
try:
    f = open('we.txt', 'r')
except Exception as result:  # Exception 会捕获错误的具体信息
    f = open('we.txt', 'w')
else:
    print('没有异常，哈哈哈')
finally:
    f.close()
    print('我就是不管你错不错都要执行我的finally语句')