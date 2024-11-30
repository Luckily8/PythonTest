"""
学到的知识：
1.raise TypeError 与 测试代码的try+except搭配使用
"""

# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：


def mul(*args):
    if len(args) == 0:
        raise TypeError("至少需要一个参数！")
    res = 1
    for i in args:
        res *= i
    return res


# 测试
print("mul(5) =", mul(5))
print("mul(5, 6) =", mul(5, 6))
print("mul(5, 6, 7) =", mul(5, 6, 7))
print("mul(5, 6, 7, 9) =", mul(5, 6, 7, 9))
if mul(5) != 5:
    print("mul(5)测试失败!")
elif mul(5, 6) != 30:
    print("mul(5, 6)测试失败!")
elif mul(5, 6, 7) != 210:
    print("mul(5, 6, 7)测试失败!")
elif mul(5, 6, 7, 9) != 1890:
    print("mul(5, 6, 7, 9)测试失败!")
else:
    try:
        mul()
        print("mul()测试失败!")
    except TypeError:
        print("测试成功!")
