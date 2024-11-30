def func1():
    print("1")


def func2():
    print("2")


def func3():
    print("3")


# 使用函数对象优化重复功能代码
dic_func = {
    "1": func1,
    "2": func2,
    "3": func3,
}

while True:
    res = input("123:")
    if res in dic_func:
        dic_func[res]()
    else:
        break
