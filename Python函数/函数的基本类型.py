# 函数的四种昂基本类型
# 1.无参数，无返回值，一般用于提示信息打印。
def myprint():
    print("-"* 10)
# 2,无参数，有返回值，多用在数据采集中，，比如获取系统信息
def mycpu():
    #获取cpu信息
    return  info
# 3，有参数，无返回值，多用在设置某些不需要返回值的参数设置
def set(a):
    pass
# 4，有参数，有返回值，一般是计算型的，需要参数，最终也要返回结果。
def cal(a,b):
    c=a+b
    return c
