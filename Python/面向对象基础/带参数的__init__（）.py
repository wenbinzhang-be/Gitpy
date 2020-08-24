# 一个类可以创建多个对象，如何对不同的对象设置不同的初始化属性
# 答： 传参数。
# 1.定义类：带参数的init：宽度和高度， 定义方法：调用实例属性
class Washer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度为{self.width}')
        print(f'洗衣机的高度为{self.height}')


# 2 创建对象，创建多个对象且属性值不同，调用实例方法
haier1 = Washer(222, 333)
haier1.print_info()
haier2 = Washer(1, 2)
haier2.print_info()
# haier3 = Washer()
# haier3.print_info()  # 不传参数会报错missing 2 required positional arguments: 'width' and ;height


