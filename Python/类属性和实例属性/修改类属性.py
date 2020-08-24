# 类属性只能通过类对象修改，不能通过实例对象修改，如果通过实例对象修改类属性，表示的是创建了一个实例属性。
class Tiger(object):
    flaw = 4


xiaohu = Tiger()
dahu = Tiger()

# 1；类 类.属性 = 值
# Tiger.flaw = 5
# print(xiaohu.flaw)
# print(dahu.flaw)


# 2.通过实例改变类属性
dahu.flaw = 2
print(Tiger.flaw)  # 4
print(xiaohu.flaw)  # 4
print(dahu.flaw)  # 2
