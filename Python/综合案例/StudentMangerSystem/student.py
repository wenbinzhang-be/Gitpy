class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'学员的名字为{self.name},学员的性别为{self.gender},学员的联系方式{self.tel}'
