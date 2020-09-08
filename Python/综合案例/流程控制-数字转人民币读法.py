'''
把一个浮点数分解为整数部分和小数部分字符串
num是需要被分解的浮点数
返回分解出来的整数部分和小数部分
第一个数组元素是整数部分，第二个数组元素是小数部分
'''


def divide(num):
    # 将一个浮点数强制类型转化为int类型，记得到它的整数部分
    integer = int(num)
    # 浮点数减去整数部分就是小数部分，小数部分乘以100后再取整，得到2位小数
    fraction = round((num-integer) * 100)
    # 下面把整数再转化为字符串
    return str(integer), str(fraction)


han_list = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
unit_list = ["十", "百", "千"]
'''
把一个4位的数字字符串变为汉字字符串
num_str是需要转换的 4 位数字字符串
返回 4 位数字字符串被转化为汉字字符串
'''


def four_to_hanstr(num_str):
    result = ""
    num_len = len(num_str)
    # 依次遍历数字字符串的每一位数字
    for i in range(num_len):
        # 把字符串转化为数值
        num = int(num_str[i])
        # 如果不是最后一位数字，而且数字不为零，则需要添加单位（千，百，十）
        if i != num_len - 1 and num != 0:
            result += han_list[num] + unit_list[num_len - 2 - i]
            pass
        pass
    # 否则不需要添加单位
    else:
        result += han_list[num]
    return result


'''
把数字字符串变成汉字字符串
num_str是需要被转换的数字字符串
返回数字字符串被转化成汉字字符串
'''


def integer_to_str(num_str):
    str_len = len(num_str)
    if str_len > 12:
        print('数字太大，翻译不了')
        return
    # 如果大于8位，包含单位 亿
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8]) + '亿' + \
            four_to_hanstr(num_str[-8: -4]) + '万' + \
            four_to_hanstr(num_str[-4:])
    # 如果单位大于4位，包含单位 万
    elif str_len > 4:
        return four_to_hanstr(num_str[-4]) + '万' + \
            four_to_hanstr(num_str[-4:])
    else:
        return four_to_hanstr(num_str)


num = float(input('请输入一个浮点数：'))
# 测试把一个浮点数分解成整数部分和小数部分
integer, fraction = divide(num)
# 测试把一个4位的数字字符串变成汉字字符串
print(integer_to_str(integer))
print(fraction)

'''
从上面的程序的运行结果来看，初步实现所需功能，但这个程序
并不是这么简单的，对于零的处理比较复杂。
例如：有两个零连接在一起时该如何处理？
还有小数部分如何翻译?
因此这个程序还需要继续完善，希望读者能把这个程序完成！！！
'''





