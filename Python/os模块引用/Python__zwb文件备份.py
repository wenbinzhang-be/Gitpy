# 需求：用户输入当前目录下任意文件名，程序完成对该文件的备份功能（备份文件名为xx皮【备份】后缀，
# 例如：test[备份].txt）
# 1.接受用户输入的文件名 sound.txt.mp3
old_name = input('请输入您要备份的文件名：')
print(old_name)
print(type(old_name))
# 2.规划备份文件名
# 2.1提取目标后缀。--找到名字中的点--名字和后缀分离--最右侧的点才是后缀的点--字符串查找某个子串 rfind
index = old_name.rfind('.')
# print(index)
# 4,思考：有效文件才备份， .txt
if index >0:
    #提取后缀
    postfix = old_name[index:]
# 2.2组织新名字= 原名字 + [备份]+后缀
# 原名字就是字符串中的一部分子串--切片【开始：结束：步长】
# print(old_name[:index])
# print(old_name[index:])
new_name = old_name[:index]+'[备份]'+postfix
print(new_name)
# 3.备份文件写入数据
# 3.1 打开 原文件 和 备份文件
old_f = open(old_name,'rb') #  rb二进制
new_f = open(new_name,'wb')
# 3.2 原文件读取，备份文件写入
# 如果不确定目标文件大小，循环读取写入，当读取出来的数据没有，终止循环
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        # 读取完成
        break
    new_f.write(con)
# 3.3 关闭文件  
old_f.close()
new_f.close()


