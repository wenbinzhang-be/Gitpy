def test_a(a, b):
    print(a+b)


# __name__是系统变量，十模块的标识符，值是：如果自身模块值是__main__;否则是当前模块的名字
if __name__ == '__main__' :
    test_a(13, 2)


