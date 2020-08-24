# 类方法特点：需要装饰器@classmethod来表示其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数
# 当方法中 需要实用类对象 （如访问私有类属性等）时，定义类方法
# 类方法一般和类属性配合使用
# # 1.定义类：私有类属性 ，类方法获取这个私有类属性
# class Dog(object):
#     __tooth = 10
#
#     # 定义类方法
#     @classmethod
#     def get__tooth(cls):
#         return cls.__tooth
#
#
# # 2.创建对象，调用类方法
# wangcai = Dog()
# result = wangcai.get__tooth()
# print(result)
# ######################1定义一个类，定义静态方法################
class wolf(object):
    @staticmethod
    def info_print():
        print('战狼')


# 2创建对象
xiaohu = wolf()

# 3,调用静态方法： 类 和 对象 都可调用
xiaohu.info_print()

wolf.info_print()
# 静态方法特点
# 1.需要通过装饰器@staticmethod来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）
# 2.静态方法 也能通过实例对象和类对象去访问
# 静态方法使用场景
# 1.当方法中 既不需要使用实例对象（如实例对象，实例属性），也不需要使用类对象（如类属性、类方法、创建实例等）时，定义静态方法
# 2.取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
