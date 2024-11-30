"""
# 1.0 字面量可以直接输入
print("text:")

# 2.0 变量无类型，数据有类型
1145.14
ikun = 1145.14
type_ikun = type(ikun)
print(type_ikun)

# 3.0  类型转换,字符转数字要求字符是数字,其余类型同理
num = "1145.14"
num = float(num)
print(type(num),num)
num = str(num)
print(type(num),num)

# 4.0 标识符规范，大小写敏感，英文选择小写且使用下划线分割

# 5.0 新的运算符：//整除，**幂运算
num = 9//2 # 4
num2 = 9.0//2.0 # 4.0
num1 = 9**2 # 81
print(num,num2,num1)
"""

# 6.0 字符串定义法：单引号(不推荐)，双引号，三引号(不用变量接收时是注释)可换行
str_1 = """ikun
  is
  atucally\n"""
"""ikun no exit:字符串包含引号几点处理：\无效"""
# str_2 = '"包含双引号的字符串"'
# str_3 = "\"使用了转义字符\、\n"
# print(str_1,str_2,str_3)
# # 字符串拼接使用+号，，号会出现空格，注意+无法连接非字符串内容
# print(str_1 + str_2)

# # 格式化表达式： f"{biaodashi}"，{}内可以包含变量或函数
# print(f"{type(str_3)}\n")

# f格式化的作用就是让{}被识别为占位符
mylist = [0, 1, 2, 3, 4]
list_1 = mylist.index(1)
print(f"1在列表中的位置是：{list_1}")

# list元素的追加
mylist.append(5)
print(mylist)
mylist.append([6, 7])
print(f"append追加[6,7]:{mylist}")
mylist.extend(["8", "9"])
print(f"extend追加[8,9]:{mylist}")

# 01:
# 1 字符串的格式化平接语法："%s  %%d %f" % (str,int,float)

# 2精度控制 %m.nf/d/s m控制"最小"宽度,n控制精度,前置空格补足宽度,后补0补足精度,优先保证精度
# #精度控制存在四舍五入
print("%2.3f" % 1145.1416)

# 02:
# input(提示信息),返回值为字符串
print(
    'input("随便写点什么:")' + "\n"
)  # 代码中，print('input("随便写点什么:")' + "\n") 只是打印了字符串 input("随便写点什么:")，并没有实际调用 input 函数来获取用户输入。

# 比较运算符号 返回值为布尔值

# str基础训练
# 联系字符串的定义与格式化,使用两种方法实现一个小任务

name = "西邮"
age = 20
time = 3
step = 1145.14
print(f"姓名:{name},年龄:{age},学习时间:{time},学习进度:{step:.1f}\n")
print("姓名:%s,年龄:%d,学习时长:%d,学习进度:%.1f\n" % (name, age, time, step))
