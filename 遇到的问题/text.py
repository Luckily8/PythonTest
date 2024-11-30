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
