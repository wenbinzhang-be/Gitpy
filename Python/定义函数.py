# 自定义一个求绝对值的my_abs函数
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
# print(my_abs(8))
# def nop():
#     pass
# import math
# def move(x,y,step,angle=0):
#     nx=x +step *math.cos(angle)
#     ny=y -step *math.sin(angle)
#     return nx,ny
# o=move(100,100,math.pi/6)
# print(o)
# -*- coding: utf-8 -*-
import math
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if b == 0 & a == 0:
        return '参数a，b不能同时为0'
    if b ** 2 - 4 * a * c < 0:
        return '该方程无解'
    elif b ** 2 - 4 * a * c == 0:
         if a == 0:
            x = (b / c)
            return x
         elif a != 0:
            x = -b / (2 * a)
            return x
    elif b ** 2 - 4 * a * c > 0:
            m = math.sqrt(b ** 2 - 4 * a * c)
            x = (-b + m) / (2 * a)
            y = (-b - m) / (2 * a)
            return x, y
# 测试
# print('quadratic(2,3,1)=',quadration(2,3,1))
# print('quadratic(1,3,-4)=',quadration(1,3,-4))
# if quadration(2,3,1) != (-0.5,-1,0):
#     print('测试失败')
#     pass
# elif quadration(1,3,-4) != (1,-4,0):
#     print('测试失败')
#     pass
# else:
#     print('测试成功')





