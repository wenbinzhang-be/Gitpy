# 1.师傅类
class Master(object):
    def __init__(self):
        self.kong_fu = '[中国古拳法形意门-闪电五连鞭]'

    def punch_print(self):
        print(f'{self.kong_fu}之我大意了，没有闪')


# 2.徒弟类
class Apprentice(Master):
    pass


# 3.创建对象
xiao_hu = Apprentice()
# 4.对象访问实例属性
print(xiao_hu.kong_fu)
# print(xiao_hu.punch_print()) 此处打印的是他的内存地址
xiao_hu.punch_print()
