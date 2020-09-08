class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
    pass


class GraduateStudent(Student):
    pass


s = Student()
s.name = 'wenbin'
s.age = 23
try:
    s.score = 99
except Exception as e:
    print(e)
g = GraduateStudent()
g.score = 99
print('g.score=', g.score)
