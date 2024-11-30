# 输入原始文件路径和目的文件路径，自动复制
# 交互
ord_side = input("What copy you want?").strip()
aim_side = input("Where should it go?").strip()
# aim_name = input('What name you want?').strip()
over_str = "Is done ,best your happy."
# 处理输入为原始字符串
r_ord_side, r_aim_side = r"{}".format(ord_side), r"{}".format(aim_side)
# 测试无误
# print(ord_side, aim_side)
# 使用for遍历line复制
with open(f"{r_ord_side}", mode="rb") as f0, open(f"{r_aim_side}", mode="wb") as f1:
    for line in f0:
        f1.write(line)
    print(over_str)
