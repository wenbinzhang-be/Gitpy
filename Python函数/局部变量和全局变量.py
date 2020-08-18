# 局部变量，就是在函数内部定义的变量【作用域仅仅局限在函数内部】
# 不同的函数 可以定义相同的局部变量，但是各自用各自的，不会产生影响
# 局部变量的作用：为了临时的保存数据，需要在函数中定义来进行存储
# ——————————————————全局变量————————————————————
# pro的定义就是一个全局变量，作用域不同
# 当全局变量和局部变量出现重复定义的时候，程序会优先执行使用函数内部的变量
pro='计算机信息管理'
name='马冬梅'
def printinfo():
    name='Peter'
    print('{}''{}'.format(name,pro))
    pass
def testmethod():
    name='张文斌'
    print(name,pro)
    pass
def changeGlobal():
    '''
    要修改全局变量
    :return:
    '''
    global pro
    pro='市场营销'
    print(pro)
    pass

changeGlobal()
testmethod()
printinfo()