class A(object):
    a = 0

    def __init__(self):
        self.b = 1

# attribute:a quality or feature of a person or things,esp.one
# that is an important part of its nature；
# eg：Self-confidence is a rare attribute in a 17-year-old
# eg: She has the physical attributes to become a championship swimmer.


aa = A()
# 返回类内部所有属性和方法对应的字典
print(A.__dict__)
# 返回实例属性和值组成的字典
print(aa.__dict__)