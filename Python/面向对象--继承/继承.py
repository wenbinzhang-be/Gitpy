# 继承： 子类默认继承父类的所用属性和方法
# 父类A
class A(object):
    def __init__(self):
        self.name = '药水哥'
        pass

    def info_print(self):
        print(self.name)
        pass


# 子类B
class B(A):
    pass


# 3 创建对象，验证结论
result = B()
result.info_print()  # 药水哥
