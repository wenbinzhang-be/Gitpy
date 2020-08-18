# 递归函数：
# 递归函数如果一个函数在内部不调用其他函数，而是自己本身，这个函数就是递归函数。
# 求阶乘，5！
# 1.循环的方式
# def jiecheng(n):
#     result=1
#     for item in range(1,n+1):
#         result*=item
#         pass
#     return result
# print('5的阶乘{}'.format(jiecheng(5)))

# 2.递归的方式
# 必须自己调用自己，必须要有结束的条件
# 优点:逻辑简单，定义简单
# 缺点：容易导致栈溢出，内存资源紧张，甚至内存泄漏
# def digui(n):
#     '''
#     递归实现
#     :param n: 阶乘参数
#     :return:
#     '''
#     if n==1:
#         return 1
#     else:
#         return n*digui(n-1)
#     pass
# 递归调用
# print('10的阶乘为：{}'.format(digui(10)))
# 递归案例：模拟实现 树型结构的遍历
import os# 引用文件操作模块
def findfile(file_path):
    listR=os.listdir(file_path)  # 得到该路径下所有的文件夹
    for fileitem in listR:
        full_path=os.path.join(file_path,fileitem)  # 获取完整的文件路径
        if os.path.isdir(full_path):  # 判断是否是文件夹
            findfile(full_path)  # 如果是一个文件夹，再次去递归
        else:
            print(fileitem)
            pass
    else:
        return
    pass
#调用搜索文件夹对象
findfile('E:\\BaiduNetdiskDownload')
