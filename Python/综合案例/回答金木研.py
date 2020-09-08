# 从1000 -7 输出直至小于7
def seven_seven():
    result = 0
    for i in range(1, 1000):
        result = 1000 - 7*i
        i += 1
        if result < 7:
            break
        else:
            print(result)


seven_seven()  # 最后一个值为13
