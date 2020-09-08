from student import *  # 我导入方式为import student，运行main时，程序报错，这是为什么


class StudentManager(object):
    def __init__(self):
        # 存储数据所用的数据--列表
        self.student_list = []

    # 一 、程序入口函数，启动程序后执行的函数
    def run(self):
        # 1.加载学员信息
        self.load_student()

        while True:
            # 2.显示功能菜单
            self.show_menu()
            # 3.用户输入功能序号
            menu_num = int(input('请输入您输入的功能序号'))
            # 4.根据用户输入的序号执行不同的功能--如果用户输入1，执行添加
            if menu_num == 1:
                # 添加学员
                self.add_student()
                pass
            elif menu_num == 2:
                # 删除学员
                self.delete_student()
                pass
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
                pass
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
                pass
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_menu()
                pass
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
                pass
            elif menu_num == 7:
                # 退出系统
                break

    # 二 定义系统功能函数，添加、删除学员等功能
    # 2.1 显示功能菜单-- 打印序号的功能对应关系 --静态
    @staticmethod
    def show_menu():
        print("请选择如下功能：")
        print("1:添加学员")
        print("2：删除学员")
        print("3：修改学员信息")
        print("4：查询学员信息")
        print("5：显示所有学员信息")
        print("6：保存学员信息")
        print("7：退出")

    # 2.2添加学员
    def add_student(self):
        # 1.用户输入姓名、性别、手机号
        name = input('请输入您的姓名')
        gender = input('请输入您的性别')
        tel = input('请输入你的电话号码')
        # 2.创建学员对象--类？类在student文件里面，先导入student模块，在创建对象
        student = Student(name, gender, tel)
        # 3. 将该对象添加到学员列表
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    # 2.3删除学员
    def delete_student(self):
        # 1.用户输入目标学员姓名
        del_name = input('请输入要删除的学员姓名')
        # 2.如果用户输入的目标学员存在则删除，否则提示学员不存在
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            print('查无此人')
        # 打印学员列表，验证删除功能
        print(self.student_list)

    # 2.4修改学员信息
    def modify_student(self):
        # 1.用户输入目标学员姓名
        modify_name = input('请输入要修改的学员的姓名：')
        # 2.如果用户输入的目标学员存在则修改姓名、性别、手机号等数据，否则提示学员不存在
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入学员姓名')
                i.gender = input('请输入学员性别')
                i.tel = input('请输入学员手机号')
                print(f'修改该学员信息成功，姓名：{i.name},性别：{i.gender},手机号：{i.tel}')
                break
        else:
            print('没有该学员的信息')

    # 2.5查询学员信息
    def search_student(self):
        # 1，用户输入目标学员姓名
        search_name = input('请输入要查询的学员的姓名')
        # 2.如果用户输入的目标学员存在，则打印出学院的信息，否则提示学员不存在
        for i in self.student_list:
            if i.name == search_name:
                print(f'您查询的学员信息为姓名：{i.name},性别：{i.gender},手机号：{i.tel}')
                break
        else:
            print('没有该学员的信息')

    # 2.6显示所有学员信息
    def show_student(self):
        print('姓名\t性别\t电话')
        for i in self.student_list:
            print(f'姓名：{i.name}\t性别：{i.gender}\t电话：{i.tel}')
        print('显示所有学员信息')

    # 2.7 保存学员信息
    def save_student(self):
        # 1打开文件
        f = open('student.data', 'w')
        # 2文件写入数据
        # 2.1[学员对象]转换成[{}]
        new_list = [i.__dict__ for i in self.student_list]
        # 2.2文件写入，字符创数据，即转换数据类型
        f.write(str(new_list))
        # 3.关闭文件
        f.close()

    # 2.8 加载学员信息
    def load_student(self):
        print('加载学员信息')
