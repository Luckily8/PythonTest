import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname='C:/Windows/Fonts/simsun.ttc')  # 这里使用的是 Windows 系统中的宋体字体

# 定义冲击序列
def impulse_sequence(n, N):
    seq = np.zeros(N)
    seq[n] = 1
    return seq

# 定义阶跃序列
def step_sequence(n, N):
    seq = np.zeros(N)
    seq[n:] = 1
    return seq

# 定义抛物线序列
def parabolic_sequence(N):
    return np.array([i**2 for i in range(N)])

# 序列参数
N = 20  # 序列长度
n = 0   # 冲击和阶跃位置从0开始

# 生成序列
imp_seq = impulse_sequence(n, N)
step_seq = step_sequence(n, N)
parab_seq = parabolic_sequence(N)

# 创建图像
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# 绘制冲击序列
axs[0].stem(range(N), imp_seq, basefmt=" ")
axs[0].set_title('单位冲击序列', fontproperties=font)
axs[0].set_xlabel('样本点', fontproperties=font)
axs[0].set_ylabel('幅值', fontproperties=font)
axs[0].grid(True)

# 绘制阶跃序列
axs[1].stem(range(N), step_seq, basefmt=" ")
axs[1].set_title('单位阶跃序列', fontproperties=font)
axs[1].set_xlabel('样本点', fontproperties=font)
axs[1].set_ylabel('幅值', fontproperties=font)
axs[1].grid(True)

# 绘制抛物线序列
axs[2].stem(range(N), parab_seq, basefmt=" ")
axs[2].set_title('单位抛物线序列', fontproperties=font)
axs[2].set_xlabel('样本点', fontproperties=font)
axs[2].set_ylabel('幅值', fontproperties=font)
axs[2].grid(True)

# 显示图像
plt.tight_layout()
plt.show()