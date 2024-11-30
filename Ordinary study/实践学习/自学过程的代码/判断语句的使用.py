# 猜数字
import random as r
# 生成一个随机数
num = r.randint(1,100)
in_1 = int(input("请输入一个1-100的整数:"))
if in_1 == num: 
    print("猜对了!")
elif in_1 < num:
    print("猜小了!")
else:
    print("猜大了!")