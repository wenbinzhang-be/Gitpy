# 在python中，抛出自定义异常的语法为raise异常类对象
# 需求：密码长度不足，则报异常（用户输入密码，如果输入的长度不足三位，则报错，即抛出自定义异常，并捕获该异常。）
# 1.自定义异常类，继承Exception ,魔法方法有 init ，str（设置异常描述信息）
class ShortInputError(Exception):
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length

    def __str__(self):
        return f'您输入的密码长度为{self.length},最少输入的密码长度为{self.min_length}'


# 2. 抛出异常,用户输入密码，如果长度小于3 ，抛出异常
def main():
    try:
        con = input('请输入您的密码')
        if len(con) < 3:
            # 抛出异常对象创建的对象
            raise ShortInputError(len(con), 3)
    except Exception as result:
        print(result)
    else:
        print('密码输入完成')


# 3，捕获该异常
main()
