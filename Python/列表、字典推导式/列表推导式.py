# list1 = [(i,j) i for i in range(1, 4)j for j in range(1,4)]
# print(list1)
# 需求，创建0-10的偶数列表
# 方法一
list2 = [i for i in range(0, 10, 2)]
print(list2)
# 方法二
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)
# 多个for循环实现列表推导式
# 需求： 创建列表如下：（1,0），（1,1），（1,2），（2,0），（2,1），（2,2）
list4 = [(i, j)for i in range(1, 3) for j in range(3)]
print(list4)
