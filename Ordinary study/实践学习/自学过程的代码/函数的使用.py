# 局部函数 计算器
def func1(n,text = input("请输入需要的功能:绝对值,平方,立方:\n")):
    def fuc_abs(x):
        return abs(x)
    def fun_squ(x):
        return x**2
    def fun_cub(x):
        return x**3
    if text == '绝对值':
        return fuc_abs(n)
    elif text == '平方':
        return fun_squ(n)
    elif text == '立方':
        return fun_cub(n)
    else:
        return '输入错误'
    
# print(func1(3))

# 匿名函数 求平方
def func2(n):
    return lambda x:x**n
fun_squ = func2(2)
print(fun_squ(3))

    