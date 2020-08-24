# 需求：警务人员与警犬一起工作，警犬分为两种，携带不同的警犬执行不同的工作


# 1.定义父类，并提供公共方法：警犬类 和 人
class Dog(object):
    def work(self):
        pass


# 2.定义子类，并重写父类方法：定义两个类表示不同的警犬
class ArmyDog(Dog):
    def work(self):
        print('追击敌人')


class DrugDog(Dog):
    def work(self):
        print('追查毒品')


# 定义人类
class Person(object):
    def work_with_dog(self, dog):
        dog.work()


# 3.创建对象传弟子类对象给调用者，可以看到不同子类执行效果不同
ad = ArmyDog()
dd = DrugDog()

zhangwenbin = Person()
zhangwenbin.work_with_dog(ad)
zhangwenbin.work_with_dog(dd)