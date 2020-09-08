# @property 广泛应用在类的定义中，可以让调用者写出简短的代码，同时能保证对参数进行必要的检查，这样就减少了程序运行时出错的可能。
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0~100！')
        self._score = value


s = Student()
s.score = 60
print('s.score=', s.score)
# ValueError：score must between 0~100！
s.score = 9999
