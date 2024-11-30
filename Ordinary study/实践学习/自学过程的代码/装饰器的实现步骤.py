# 逐渐实现需求，并优化代码，体会装饰器的实现步骤与应用场景
# 原代码：
def func1(str1):
    print(str1)


def func2(str2):
    print(str2)


# func1("hello")
# func2("bye")

# 需求：1，增加功能，代码运行完成后输出一句over,2，不改变原代码,源码参数不固定 3，不改变调用方式
# 4，可复用 ，5.细节性要求，如保证help是原函数
# 方案一：直接改变源码===只能实现1,增加功能
pass


# 方案二：使用函数封装原函数===实现1,2,不改变原代码,源码参数不固定
# def wrapper1(*args, **kwargs):
#     res = func1(*args, **kwargs)
#     print("over".center(50, "="))
#     return res


# wrapper1("hello")


# 方案三：作为函数对象返回===实现1,2,3,不改变调用方式
def deco_new(func1):
    def wrapper2(*args, **kwargs):
        res = func1(*args, **kwargs)
        print("over".center(50, "="))
        return res

    return wrapper2


print(func1)
func1 = deco_new(func1)
print(func1)
func2 = deco_new(func2)
func1("hello")
func1("hel2lo")
func2("bye")


# 方案四：使用闭包函数===实现1,2,3,4,可复用

# 方案五：使用内置快捷功能===实现所有需求

import functools


def builtin_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("over".center(50, "="))
        return res

    return wrapper
