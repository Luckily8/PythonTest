import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 创建折线图
plt.plot(x, y)

# 添加标题和标签
plt.title('简单折线图示例')
plt.xlabel('X 轴标签')
plt.ylabel('Y 轴标签')

# 显示图像
plt.show()