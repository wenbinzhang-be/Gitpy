# 1.师傅类
class Master(object):
    def __init__(self):
        self.kong_fu = '[中国古拳法之闪电五连鞭]'

    def teach_lesson(self):
        print(f'{self.kong_fu}唯一传人马保国')


# 2.创建学校类
class School(Master):
    def __init__(self):
        self.kong_fu = '[现代化拳法之闪电五连鞭]'

    def teach_lesson(self):
        print(f'{self.kong_fu}之教头马保国')

        # 2.1 super()调用
        # super(School, self).__init__()
        # super(School,self).teach_lesson()

        # 2.2无参数的super
        super().__init__()
        super().teach_lesson()


class Prentice(School):  # 当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法,如果不同则都继承
    def __init__(self):
        self.kong_fu = '[自创改造闪电五连鞭]'

    def teach_lesson(self):
        # 加上自己的初始化的原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值
        self.__init__()
        print(f'{self.kong_fu}之改一个动作就算我自创')
    pass

    # 需求： 一次性调用父类school master的方法
    def make_old_cake(self):
        # 方法1 如果定义的类名要修改，这里代码需要频繁更改
        # School.__init__(self)
        # School.teach_lesson(self)
        # Master.__init__(self)
        # Master.teach_lesson(self)
        #
        #
        # 方法二：super（）
        # 方法2.1 super（当前类名，self）.函数调用
        # super(Prentice, self).__init__()
        # super(Prentice, self).teach_lesson()
        # 方法2.2 无参数super().函数（）
        super().__init__()
        super().teach_lesson()
# 使用super() 可以自动查找父类。调用顺序遵循_mro__类属性的顺序。比较适合单继承使用


daqiu = Prentice()
daqiu.make_old_cake()