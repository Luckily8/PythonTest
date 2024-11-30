# 实时监测文件是否有新增，有则输出
# 交互
out_log = "监测到新日志...\n"
# 监测
with open("Ordinary study\堆栈区\log_text.txt", mode=("+ab")) as f:
    # 移动指针
    findex = f.tell()
    # new log
    need_new = input("是否新增日志？输入True or False\n").strip()
    if (need_new == "True") or (need_new == "true"):
        need_new = True
    else:
        need_new = False
    while need_new:
        new_log = input("Waiting for insert：\n").strip().encode("UTF-8")
        f.write(new_log + "\n".encode("UTF-8"))
        # 判断是否新增 and 输出显示
        if findex != f.tell():
            f.seek(findex, 0)
            print(out_log + "\n")
            print("new log is:", f.read().decode("UTF-8"))
            print("".center(50, "*"))
            findex = f.tell()

        need_new = input("是否新增日志？输入True or False\n").strip()
        if (need_new == "True") or (need_new == "true"):
            need_new = True
        else:
            need_new = False
