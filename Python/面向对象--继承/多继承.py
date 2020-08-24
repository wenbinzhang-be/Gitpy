# 1.师傅类
class Master(object):
    def __init__(self):
        self.kong_fu = '[中国古拳法之闪电五连鞭]'

    def teach_lesson(self):
        print(f'{self.kong_fu}唯一传人马保国')


# 2.创建学校类
class School(object):
    def __init__(self):
        self.kong_fu = '[系统化学习闪电五连鞭]'

    def teach_lesson(self):
        print(f'{self.kong_fu}之教头马保国')

    def zichuang(self):
        print(f'{self.kong_fu}不要再骗我这个老同志了')


class Prentice(Master, School):  # 当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法,如果不同则都继承
    def __init__(self):
        super().__init__()
        self.kong_fu = '[自学闪电五连鞭]'

    def teach_lesson(self):
        print(f'{self.kong_fu}之改一个动作就算我自创')

    pass


xiaozhang = Prentice()
print(xiaozhang.kong_fu)
xiaozhang.teach_lesson()
xiaozhang.zichuang()
print(Prentice.__mro__)  # 看到当前类的层级和继承关系
# 如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，调用到的是子类里面的同名属性和方法


