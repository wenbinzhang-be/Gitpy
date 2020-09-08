class Master():
    def __init__(self):
        self.kongfu = '[初级前饼果子配方]'

    def make_cake(self):
        print(f'{self.kongfu}之老师傅自创')


class School(object):
    def __init__(self):
        self.kogfu = '[中级煎饼果子配方]'

    def make_cake(self):
        print(f'{self.kogfu}之学校秘制配方')


class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[高级煎饼果子配方]'
        # self.money = 200000  # 共有属性
        self.__money = 2000  # 私有属性

    # 定义函数：获取私有属性值，get__xx
    def get__money(self):
        return self.__money

    # 定义函数： 修改私有属性值，set__xx
    def set__money(self):
        self.__money += 500

    # 定义私有方法
    def __info_print(self):
        self.cash = '两万元'
        print('这是私有方法')

    def make_cake(self):
        print(f'{self.kongfu}之缝合怪自创')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(Prentice):
    pass


xiaohu = Tusun()
print(xiaohu.get__money())
xiaohu.set__money()
print(xiaohu.get__money())



