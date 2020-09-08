from tkinter import *
# 创建Tk对象，Tk代表窗口
root = Tk()
# 设置窗口标题
root.title('窗口标题')
# 创建 label对象，第一个参数指定将该label放入root内
w = Label(root, text='HELLO,TKINTER!')
# 调用pack进行布局
w.pack()
# 启动主窗口
root.mainloop()
