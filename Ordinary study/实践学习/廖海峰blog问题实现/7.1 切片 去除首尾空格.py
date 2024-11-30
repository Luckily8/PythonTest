# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    # 处理输入为空，避免索引越界
    if s == "":
        return ""
    # 找到边缘
    i_fron = 0
    i_late = -1
    # 分割
    while True:  # 按位判断是否为空
        if s[i_fron] == " ":
            i_fron += 1
            if i_fron == len(s):
                s = ""
                break
            continue
        # 处理首部
        else:
            s = s[i_fron:]
            break
    # 处理长度为空，避免索引越界
    if s == "":
        return ""
    while True:  # 按位判断是否为空
        if s[i_late] == " ":
            i_late -= 1
            if i_late == -len(s):
                s = ""
                break
            continue
        # 处理尾部
        elif i_late == -1:
            s = s[:]
            break
        else:
            s = s[: i_late + 1]
            break
    return s


# 测试:
if trim("hello  ") != "hello":
    print("测试1失败!")
elif trim("  hello") != "hello":
    print("测试2失败!")
elif trim("  hello  ") != "hello":
    print("测试3失败!")
elif trim("  hello  world  ") != "hello  world":
    print("测试4失败!")
elif trim("") != "":
    print("测试5失败!")
elif trim("    ") != "":
    print("测试6失败!")
else:
    print("测试成功!")

""" 学到的知识：
1. 空字符串无法使用-1索引
2. 使用索引取值时，一定要注意越界问题，每次对象长度发生变化后都要检查
3. 在函数接受参数的一开始，就要想好分类依据
4. 切片不包含stop索引
5. 使用逆向索引时需要考虑是否超出逆向范围
6. s[: i_late + 1]在i_late==-1时返回空字符，需要分类处理
7. 切片操作不会因为索引越界而抛出错误。相反，Python 会根据提供的索引和步长返回一个合理的结果，即使索引超出实际范围。
8. 对负值重新理解切片：[start:stop:step] 
"""
# 大佬方案学习：递归
"""
1.分类依据选择len
2.使用递归，按位递进，减少s长度，直至长度为0 或满足条件
def trim(s):
    if len(s) > 0:
        if s[0] == " ":
            return trim(s[1:])
        elif s[-1] == " ":
            return trim(s[:-1])
        else:
            return s
    else:
        return s
"""
# AI方案学习：迭代
"""
1.避免了递归，提高了代码的效率和可读性
2.当字符串很长时，可能会导致递归调用过深，影响性能。您可以考虑使用迭代的方式来替代递归，这样可以提高效率并减少栈内存的消耗
3.s[1:1] == 空
def trim(s):
    if s == '':
        return s
    start = 0
    end = len(s) - 1
    while start <= end and s[start] == ' ':
        start += 1
    while end >= start and s[end] == ' ':
        end -= 1
    return s[start:end+1]

"""
s = "1234"
print("输出为空:", s[-100:-2:100])
