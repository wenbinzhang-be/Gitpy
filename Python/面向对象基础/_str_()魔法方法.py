# 当使用print输出对象的时候，默认打印对象的内存地址。如果类定义了_str_方法，那么就会打印从这个方法中return的数据
class Washer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return '我不使用海尔电器'
    

haier = Washer(10, 20)
print(haier)
