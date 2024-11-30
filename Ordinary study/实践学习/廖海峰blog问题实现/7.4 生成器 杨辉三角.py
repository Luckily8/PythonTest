""" 杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
"""

"""学到的知识：
1. 列表可以使用+运算拼接，前提是+连接的是list类型
2. 有时候拼接操作并不能用其他方式替代
3. AI方法避免了显式的循环索引操作，使代码更具 Python 风格（Pythonic）
4. zip()函数可以将两个列表对应位置相加
5. map(lambda ,a,b)函数lambda并非只能接受一个参数
6.map() 函数可以接受多个可迭代对象（iterable）作为参数，当传入多个 iterable 时，lambda 函数需要有相应数量的参数
"""


def triangles():
    # 处理初始化
    res, n = [1], 0
    yield res
    res, n = [1, 1], 1
    yield res
    # 生成算法
    while True:
        n += 1
        # 当前行的运算次数与上一行的层数差1，生成表达式是最直接的方法
        res = [1] + [res[i] + res[i + 1] for i in range(n - 1)] + [1]
        yield res


n = 0
results = []
for t in triangles():
    results.append(t)
    print(results)
    n = n + 1
    if n == 10:
        break
print("测试通过!")

"""AI答案：
### 方法一：使用 append() 方法构建新列表
def triangles():
    res = [1]
    while True:
        yield res
        next_row = [1]  # 开头的 1
        for i in range(len(res) - 1):
            next_row.append(res[i] + res[i + 1])  # 中间的元素
        next_row.append(1)  # 结尾的 1
        res = next_row

### 方法二：使用 zip() 函数
思路：
示例：

假设当前行 res = [1, 2, 1]，那么：

a = [0, 1, 2, 1]
b = [1, 2, 1, 0]
在 res 前后各添加一个 0，形成两个新列表：
a = [0] + res
b = res + [0]
使用 zip() 函数将 a 和 b 中的元素配对相加，得到下一行。
def triangles():
    res = [1]
    while True:
        yield res
        res = [x + y for x, y in zip([0]+res, res+[0])]

### 方法三：使用 map() 函数和匿名函数
思路：
与方法二类似，利用 map() 函数对前后添加了 0 的列表进行元素相加。
def triangles():
    res = [1]
    while True:
        yield res
        res = list(map(lambda x, y: x + y, [0]+res, res+[0]))
"""
