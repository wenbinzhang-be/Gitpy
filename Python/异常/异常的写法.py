# 2.1 语法
# try：
#     可能发生错误的代码
# expect：
#     如故出现异常执行的代码
# 2.2 快速体验
# 需求：尝试以r模式打开文件，如果文件不存在，则以w方式打开
try:
    f = open('we.txt', 'r')
except:
    f = open('we.txt', 'w')
