"""
学到的知识：
1.如果有必要，可以先对参数的数据类型做检查 reaise Typeerror。。。
2.函数可以返回多个值，本质上返会一个tuple
3.hex函数返回str类型
"""

# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1 = 255
n2 = 1000
print("n1:", type(hex(n1)), "n2:", str(hex(n2)))


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 的两个解。
# 提示：
# 一元二次方程的求根公式为：
# 计算平方根可以调用math.sqrt()函数：
import math


def quadratic(a, b, c):
    if a == 0:
        return "error"
    derta = b**2 - 4 * a * c
    res1 = (-b + math.sqrt(derta)) / (2 * a)
    res2 = (-b - math.sqrt(derta)) / (2 * a)
    return res1, res2


# 测试:
print("quadratic(2, 3, 1) =", quadratic(2, 3, 1))
print("quadratic(1, 3, -4) =", quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print("测试失败")
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print("测试失败")
else:
    print("测试成功")
