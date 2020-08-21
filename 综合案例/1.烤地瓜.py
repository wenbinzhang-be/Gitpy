# 1.定义类：初始化属性，被烤和添加调料的方法，显示对象信息的str
class SweetTomato():
    def __init__(self):
        # 1.被烤时间
        self.cook_time = 0
        # 2.地瓜状态
        self.cook_status = '生的'
        # 3.添加调料
        self.condiments = []  # 列表存储

    def cook(self, time):
        self.cook_time += time  # 累计时间去进行条件判断
        # 通过时间去判断状态
        if 0 <= self.cook_time < 3:
            self.cook_status = '生的,不能吃呢'
            pass
        elif 3 <= self.cook_time < 5:
            self.cook_status = '半生不熟 ，还不能吃呢'
            pass
        elif 5 <= self.cook_time < 8:
            self.cook_status = '地瓜熟了，可以吃了呢'
            pass
        elif self.cook_time >= 8:
            self.cook_status = '地瓜烤糊了，可以扔了呢'
            pass

    def add_condiment(self, condiment):
        """添加调料"""
        # 用户意愿的调料追加到调料列表
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜被考过的时间是{self.cook_time},这个地瓜的状态为{self.cook_status},调料有{self.condiments}'


# 2.创建对象并调用对应的实例方法
di_gua1 = SweetTomato()
di_gua1.cook(5)
di_gua1.add_condiment('酸菜包')
print(di_gua1)
di_gua1.add_condiment('辣椒面')
print(di_gua1)
