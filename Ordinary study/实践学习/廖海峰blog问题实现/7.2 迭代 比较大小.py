# 请使用迭代查找一个list中最小和最大值，并返回一个tuple,注意不调用内置max，min函数


def findMinAndMax(L):
    # 解决长度为空，避免索引溢出
    if len(L) == 0:
        return (None, None)
    # 不为空，获取初值，开始迭代比较
    l_min = L[0]
    l_max = L[0]
    for i in L:
        if i >= l_max:
            l_max = i
        if i <= l_min:
            l_min = i

    return (l_min, l_max)


print(findMinAndMax([]))

# 测试
if findMinAndMax([]) != (None, None):
    print("测试失败!")
elif findMinAndMax([7]) != (7, 7):
    print("测试失败!")
elif findMinAndMax([7, 1]) != (1, 7):
    print("测试失败!")
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print("测试失败!")
else:
    print("测试成功!")
