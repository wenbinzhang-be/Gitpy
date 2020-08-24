# 当删除对象时，Python解释器也会默认调用_del_()方法
class Delete(object):
    def __init__(self):
        self.wwf = 22

    def __del__(self):
        print('对象已经被删除')


ha_ier1 = Delete()
print(ha_ier1)
