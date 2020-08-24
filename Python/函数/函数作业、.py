# 1.写函数，接受n个数字，求这些参数数字的和
# %d整形 格式化输出
def sumall(*args):
    result = 0
    for item in args:
        result += item
        pass
    print('您输入的和=%d' % result)


sumall(1, 2, 3, 4, 5, 6, 6)


# %f浮点型 格式化输出
def sumall(*args):
    result = 0
    for item in args:
        result += item
        pass
    print('您输入的和=%s' % result)


sumall(1, 2, 3, 4, 5, 6, 6.1)

# 2.写函数，找出传入列表或元组的奇数位所对应的元素，并返回一个新的列表
list1=(1,2,3,4,5,6,7,8)
def findyou(con):
    list1=[]
    index=0
    for i in con:
        if index%2==1:
            list1.append(i)
            pass
        index+=1
    return list1
    pass
ok=findyou([1,2,3,4,5,6])
print(ok)
r=findyou(tuple(range(10,30)))
print(r)



# 3.写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将信的内容返回给调用者，
# ps:字典中的value只能是字符串或者列表
def cutyou(cutff):
    result={}#空列表
    for key,value in cutff.items():
        if len(value)>3:
            result[key]=value[:3]
            pass
        else:
            result[key]=value
            pass
        pass
    return result
    pass
ra={'name':'张文斌','age':'24','hooby':['basketball','swimming','hiking','climing']}
print(cutyou(ra))

