# 文件指针限制查找次数
with open("Ordinary study\text_passwrd.txt", mode="rt", encoding="UTF-8") as f:
    for x in range(3):
        res = f.read
        in_name = input("请输入用户名：").strip()
        in_pass = input("inter your digital password:").strip()
        if not in_pass.isdigit():
            print("！！！喂小鬼，乱填可就遭老罪咯~")
        else:
            in_pass = int(in_pass)
            for user in f:
                print("遍历中.....")
                cor_name = user.strip().split(":")[0]
                cor_pass = int(user.strip().split(":")[1])
                print(cor_name, cor_pass)
                if in_name == cor_name and in_pass == cor_pass:
                    print("welcome!!!".center(50, "="))
                    break  # 循环需要重新恢复文件指针
                else:
                    continue
            else:
                print("no correctly,bye~".center(50, "X"))
        if x == 2:
            print("is time out of 3...")
            break

# 无限次循环查找
name_pass = {}
with open("Ordinary study\passwrd.txt", mode="rt", encoding="UTF-8") as f:
    for user in f:
        # print("读取数据库中.....")
        cor_name = user.strip().split(":")[0]
        cor_pass = int(user.strip().split(":")[1])
        name_pass[cor_name] = cor_pass
        # print(name_pass)
for x in range(10):
    in_name = input("inter your name：").strip()
    in_pass = input("inter your digital password:").strip()
    if not in_pass.isdigit():
        print("！！！喂小鬼，乱填可就遭老罪咯~")
    else:
        in_pass = int(in_pass)
        for cor_name in name_pass:
            print("寻找用户中...", cor_name)
            if in_name == cor_name and in_pass == name_pass[cor_name]:
                print("  welcome!!!  ".center(80, "="))
                break
            else:
                continue
        else:
            print("  no correctly,bye~  ".center(80, "X"))
    if x == 2:
        print("\n祝你每天都开心~")
        break
