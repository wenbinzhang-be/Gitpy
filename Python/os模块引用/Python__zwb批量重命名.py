# 需求1，把code文件夹所有文件重命名 Python__zwb
# 需求2，删除Python__zwb重命名
import os
flag = 0
# 1.找到所有文件：获取code文件夹的目录列表 --listdir
file_list = os.listdir()
print(file_list)
# 2.构造名字
for i in file_list:
    if flag == 0:
        new_name = 'Python__zwb' + i
    elif flag == 1:
        num = len('Python__zwb')
        new_name = i[num:]
    # 3.重命名
    os.rename(i, new_name)
