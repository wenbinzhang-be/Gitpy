# 1.师傅类
class Master(object):
    def __init__(self):
        self.kong_fu = '[中国古拳法之闪电五连鞭]'

    def teach_lesson(self):
        print(f'{self.kong_fu}唯一传人马保国')


# 2.创建学校类
class School(object):
    def __init__(self):
        self.kong_fu = '[现代化拳法之闪电五连鞭]'

    def teach_lesson(self):
        print(f'{self.kong_fu}之教头马保国')


class Prentice(Master, School):  # 当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法,如果不同则都继承
    def __init__(self):
        self.kong_fu = '[自创改造闪电五连鞭]'

    def teach_lesson(self):
        # 加上自己的初始化的原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值
        self.__init__()
        print(f'{self.kong_fu}之改一个动作就算我自创')
    pass

    # 子类使用父类的同名方法和属性：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        # 父类类名，函数（）
        # 再次调用初始化的原因：这里想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        # self：接受将来调用这个函数的对象
        Master.__init__(self)
        Master.teach_lesson(self)

    def make_school_cake(self):
        School.__init__(self)
        School.teach_lesson(self)


xiaozhang = Prentice()
xiaozhang.teach_lesson()
xiaozhang.make_school_cake()
xiaozhang.make_master_cake()
xiaozhang.teach_lesson()




