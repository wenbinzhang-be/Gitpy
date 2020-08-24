class Master(object):
    def __init__(self):
        self.kong_fu = '[中国古拳法之闪电五连鞭]'

    def teach_lesson(self):
        print(f'{self.kong_fu}唯一传人马保国')


class School(object):
    def __init__(self):
        self.kong_fu = '[现代化拳法之闪电五连鞭]'

    def teach_lesson(self):
        print(f'{self.kong_fu}之教头马保国')


class Prentice(Master, School):
    def __init__(self):
        super().__init__()
        self.kong_fu = '[自创改造闪电五连鞭]'

    def teach_lesson(self):
        self.__init__()
        print(f'{self.kong_fu}之改一个动作就算我自创')
    pass

    def make_master_cake(self):
        Master.__init__(self)
        Master.teach_lesson(self)

    def make_school_cake(self):
        School.__init__(self)
        School.teach_lesson(self)


# 徒孙类
class Tusun(Prentice):
    pass


xiaoqiu = Tusun()
xiaoqiu.teach_lesson()
xiaoqiu.make_master_cake()
xiaoqiu.make_school_cake()
