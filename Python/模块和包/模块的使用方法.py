# 需求 ：math模块下sqrt（） 开平方计算
# 方法一 ：import 模块名；模块名.功能
# import math
# print(math.sqrt(9))  # 3.0 为什么是3.0,python里只要有出现除法，一定是浮点数。
# 方法二： from 模块名 import 功能1 ，功能2，功能3...;调用方功能直接调用
# from math import sqrt
# print(sqrt(9))
# 方法三： from ..import *;功能调用
# from math import *
# print(sqrt(9))
# as定义别名
# # 模块定义别名
# import 模块名 as别名
# # 功能定义别名
# from 模块名 import 功能 as 别名
# 模块别名
import time as tt
tt.sleep(2)
# time.sleep(2) # name time is not defined,
print('hello')


# 功能别名
from math import sqrt as aa
print(aa(4))
