# 1 导入进程包
import multiprocessing
import time


def dance():
    for i in range(3):
        print('跳舞中')
        time.sleep(0.2)


def sing():
    for i in range(3):
        print('唱歌中')
        time.sleep(0.2)


# 2. 创建子进程（自己手动创建的进程为子进程）
# 1.group: 进程组，目前只能使用None，一般不需要说明
# 2.target：进程执行的目标任务
# 3.name：进程名，如果不设置，默认Process-1.......
dance_process = multiprocessing.Process(target=dance)
sing_process = multiprocessing.Process(target=sing)
# 3.启动进程执行对应的任务
dance_process.start()
dance_process.start()

# 进程执行时无序的，具体哪个进程先执行是有操作系统调度决定
