# 慧智满天繁星
import numpy as np
import matplotlib.pyplot as plt

# 设置星星的数量
num_stars = 1000

# 生成随机的星星位置和亮度
x = np.random.rand(num_stars)
y = np.random.rand(num_stars)
brightness = np.random.rand(num_stars)

# 创建一个黑色背景的图
fig, ax = plt.subplots()
ax.set_facecolor('black')

# 绘制星星
ax.scatter(x, y, s=brightness*100, c='white', alpha=0.8)

# 去掉坐标轴
ax.set_xticks([])
ax.set_yticks([])

# 显示图像
plt.show()