# # 体验异常传递
# 需求：
# 1.尝试只读方式打开test.txt文件，如果文件存在则读取文件内容，文件不存在则提示用户即可
# 2.读取内容要求：尝试循环内容，读取过程中如果检测到用户意外终止程序，则except捕获异常并提示用户
import time
try:
    f = open('we.txt')
    # 尝试循环读取数据
    try:
        while True:
            content = f.readline()
            # 如果数据读取完成退出循环
            if len(content) == 0:
                break
            time.sleep(3)
            print(content)
    except:
        # 在命令提示符中如果按下ctrl+c 结束终止的键
        print('意外终止了读取数据')
    finally:
        f.close()
        print('文件关闭')
except:
    print('我就是你上面出错时需要执行我的expect语句')



