import time

# 实时监测文件是否有新增，有则输出
# 交互
out_log = "监测到新日志...\n"
# 监测
with open("Ordinary study\\堆栈区\\log_text.txt", mode="r+", encoding="UTF-8") as f:
    # 移动指针到文件末尾
    findex = f.tell()
    while True:
        try:
            # # 获取当前文件指针位置
            # current_position = f.tell()
            # 移动指针到文件末尾
            f.seek(0, 2)  # 另法：f.readline() ,len() != 0
            end_position = f.tell()
            if findex != end_position:
                f.seek(findex, 0)
                print(out_log + "\n")
                res = f.read()
                print("new log is:", res)
                print("".center(50, "*"))
                findex = f.tell()
            time.sleep(1)  # 添加短暂的睡眠时间，减少 CPU 占用
        except KeyboardInterrupt:
            print("监测已中断")
            break
