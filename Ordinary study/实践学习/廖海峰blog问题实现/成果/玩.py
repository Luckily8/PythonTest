import os

# 打印当前工作目录
print("当前工作目录:", os.getcwd())

# 构建文件路径
file_path = os.path.join('H:\\', 'Library', '知识', 'pythonText', 'Python全栈', 'xyj.txt')

# 确保输出目录存在
output_dir = os.path.join('H:\\', 'Library', '知识', 'pythonText', 'Python全栈', 'result')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 使用构建的路径打开文件，并指定编码为 UTF-8
try:
    with open(file_path, 'r', encoding='utf-8') as fr:
        # 读取和处理文件内容
        ...
except FileNotFoundError:
    print(f"文件未找到: {file_path}")