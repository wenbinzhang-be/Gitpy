# 1、自己的文件名不能喝已有模块名重复，如果重复会导致模块无法使用 --random
# import random
# num = random.randint(1, 4)
# print(num)
# 为什么？ 因为python解释器会从自己目录下搜索
# 2， 使用from模块名 import功能，导入模块功能，如果工能名字重复，导入的时候定义或后倒入的这个同名功能
# 场景 time.sleep()

# 定义函数 sleep
# def sleep():
#     print('我是定义的sleep')
#
#
# from time import sleep
# sleep(2)


# 拓展： 名字重复
# 问题： import 模块名字 是否担心，功能名字重复的问题--不需要
import time  # 模块
print(time)


time = 1  # 变量会覆盖模块的功能
print(time)
# 为什么变量能覆盖模块功能》？-.-在python中，数据是通过-引用-传递的。
open('包.txt','w')