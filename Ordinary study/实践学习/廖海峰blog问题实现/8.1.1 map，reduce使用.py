# 匿名函数map，reduce的使用

from functools import reduce

# map 实现非法转化为标志字符
res = ["NAME", "ABCD", "EFG"]
norname = map(lambda s: s[0].upper() + s[1:].lower(), res)
for i in norname:
    print(i, norname)

# reduce 实现连乘积
res = [1, 2, 3, 4, 5, 6]
prod = reduce(lambda x, y: x * y, res)
print(prod)

# map+reduce 实现字符串转换浮点数字
my_dict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def str2float(str_2):

    str_2 = str_2.split(".")
    str2list1 = map(lambda x: my_dict[x], str_2[0])
    str2list2 = list(map(lambda x: my_dict[x], str_2[1]))
    res1 = reduce(lambda x, y: x * 10 + y, str2list1)
    res2 = reduce(lambda x, y: x * 10 + y, str2list2) / (
        10 ** len(str2list2)
    )  # 快速算法
    i_index = 0

    # res2 = reduce(
    #     float_lambda, str2list2
    # )  # 小数套乘十相加算法是不对的
    def calc(z):
        nonlocal i_index
        i_index -= 1
        return z * 10**i_index

    # res2 = reduce(lambda x, y: x + y, map(calc, str2list2))
    # res2 = reduce(lambda x,y:x+y,map(lambda z:i_index-=1;z*10(i_index),str2list2)) lambda只能加一条语句
    return res1 + res2


print(str2float("1145.1411246"))
# ai优化
from functools import reduce


def str2float(s):
    int_part, frac_part = s.split(".")
    int_num = reduce(lambda x, y: x * 10 + y, map(int, int_part))
    frac_num = reduce(lambda x, y: x * 10 + y, map(int, frac_part))
    return int_num + frac_num / (10 ** len(frac_part))


print(str2float("1145.1411246"))
