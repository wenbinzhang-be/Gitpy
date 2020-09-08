# 方法一
"""
1.导入
import 包名.模块名
2.调用功能
包名.模块名.功能（）
"""
# import my_package.my_module11
#
# my_package.my_module11.info_print2()
# 方法二 设置__init__.py文件里面的all列表，添加的时允许导入的编排
"""
from 包名 import *
模块名.目标
"""
from my_package import *
my_module11.info_print1()
# 注意： 必须在__init__.py文件中添加__all__ = []：控制允许导入的模块列表
