class Dog(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


p = Dog('张文斌', 23)
print(p.name)
print(p.age)
p.name = '张武斌'
p.age = 32
print(p.name, p.age)
