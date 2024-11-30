import matplotlib.pyplot as plt

# 等差数列
def arithmetic_sequence(a, d, n):
    return [a + d * i for i in range(n)]

# 等比数列
def geometric_sequence(a, r, n):
    return [a * r ** i for i in range(n)]

# 斐波那契数列
def fibonacci_sequence(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

# 序列参数
n = 10  # 序列长度
a = 1   # 初始值
d = 2   # 等差数列的公差
r = 2   # 等比数列的公比

# 生成序列
arith_seq = arithmetic_sequence(a, d, n)
geom_seq = geometric_sequence(a, r, n)
fib_seq = fibonacci_sequence(n)

# 创建图像
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# 绘制等差数列
axs[0].stem(range(n), arith_seq)
axs[0].set_title('等差数列')
axs[0].set_xlabel('样本点')
axs[0].set_ylabel('值')
axs[0].grid(True)

# 绘制等比数列
axs[1].stem(range(n), geom_seq)
axs[1].set_title('等比数列')
axs[1].set_xlabel('样本点')
axs[1].set_ylabel('值')
axs[1].grid(True)

# 绘制斐波那契数列
axs[2].stem(range(n), fib_seq)
axs[2].set_title('斐波那契数列')
axs[2].set_xlabel('样本点')
axs[2].set_ylabel('值')
axs[2].grid(True)

# 显示图像
plt.tight_layout()
plt.show()