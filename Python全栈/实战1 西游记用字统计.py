import os

# 打印当前工作目录
print("当前工作目录:", os.getcwd())

# 构建文件路径
file_path = os.path.join('H:\\', 'Library', '知识', 'pythonText', 'Python全栈', 'xyj.txt')
output_dir = os.path.join('H:\\', 'Library', '知识', 'pythonText', 'Python全栈', 'result')
# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# try
try:
    with open(file_path, 'r', encoding='utf-8') as fr:
        # 读取和处理文件内容
        ... #约等于 pass
except FileNotFoundError:
    print(f"文件未找到: {file_path}")

# 使用构建的路径打开文件，并指定编码为 UTF-8
with open(file_path, 'r', encoding='utf-8') as fr:
    characters = []
    stat = {}

    for line in fr:
        # 去掉每一行两边的空白
        line = line.strip()
        # 如果为空行则跳过该轮循环
        if len(line) == 0:
            continue
        # 遍历该行的每一个字
        for x in range(len(line)):
            # 去掉标点符号和空白符
            if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
                continue
            # 尚未记录在characters中
            if line[x] not in characters:
                characters.append(line[x])
            # 尚未记录在stat中
            if line[x] not in stat:
                stat[line[x]] = 0
            # 汉字出现次数加1
            stat[line[x]] += 1

print(len(characters))
print(len(stat))

# lambda生成一个临时函数
# d表示字典的每一对键值对，d[0]为key，d[1]为value
# reverse为True表示降序排序
stat = sorted(stat.items(), key=lambda d: d[1], reverse=True)

# 将结果写入指定路径的 CSV 文件
output_path = os.path.join(output_dir, 'result of 西游记用字统计.csv')
with open(output_path, 'w', encoding='utf-8') as fw:
    for item in stat:
        # 进行字符串拼接之前，需要将int转为str
        fw.write(item[0] + ',' + str(item[1]) + '\n')

# 打印前10个字和出现次数,后10个字和出现次数,每输出一个字就换行
print("前10个字和出现次数:")
for i in range(10):
    print(stat[i])
print("后10个字和出现次数:")
for i in range(10):
    print(stat[-i-1])

