"""
学到的知识：三步骤-不满足-三步走-满足，每次hannota都假设辅助是空的，只需要满足另外两个完成队规在考虑辅组
1.代码的注释一把使用单行注释，多行注释避免包含代码块
2.递归：
对于递归来说，你要是非要展开思考的它的中间过程，那么就是自讨苦吃，这也违背了递归的初心。

按照递归的思路，我们只需要考虑n和n-1的关系就好了，至于n-2,n-3...完全没必要考虑。

就像外包一样，甲方分一部分给外包，外包再分一部分给小型创业外包公司一个道理。根本不需要知道小外包怎么实现的，只要它干完就相当于这个模块完成了。

回到正题：

一层，逻辑肯定是 A->C,

那么二层是什么？答案是：在一层的基础上，将第一层全部移到B上，这个时候A只剩一块了，那么将A->C,然后再将所有的B->C。结束

那么三层是什么？在二层的基础上重复上述逻辑。
递归不要考虑复杂了，本身就是一个很简单的东西，我愿意称最简单的算法，没有之一，全天下所有的递归都是一个算法，只用找到n是n-1通过什么逻辑到达的即可。这个逻辑就是递归的逻辑。

2就是1+1得到的 3就是2+1得到的

f(n)就是f(n-1)+逻辑得到的，仅此而已。
"""

# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。

# fact(5)对应的fact_iter(5, 1)的调用如下：

# => fact_iter(5, 1)
# => fact_iter(4, 5)
# => fact_iter(3, 20)
# => fact_iter(2, 60)
# => fact_iter(1, 120)
# => 120
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出
"""hanota 问题
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')
"""


def hanota(n, a, b, c):
    if n == 1:
        print(a, "===>", c)
    else:  # 上层移动到b,a--b
        hanota(n - 1, a, c, b)  # 注意位置的1变化
        # 此时A层数等于1,a--c
        hanota(1, a, b, c)
        # 此时回头解决b--c
        hanota(n - 1, b, a, c)


hanota(3, "A", "B", "C")
# 递归展开：

# 第一次调用： hanota(3, "A", "B", "C")

# 步骤1： hanota(2, "A", "C", "B")

# 第二次调用： hanota(2, "A", "C", "B")

# 步骤1： hanota(1, "A", "B", "C")

# 第三次调用： hanota(1, "A", "B", "C")
# 打印： A ===> C
# 步骤2： hanota(1, "A", "C", "B")

# 第四次调用： hanota(1, "A", "C", "B")
# 打印： A ===> B
# 步骤3： hanota(1, "C", "A", "B")

# 第五次调用： hanota(1, "C", "A", "B")
# 打印： C ===> B
# 步骤2： hanota(1, "A", "B", "C")

# 第六次调用： hanota(1, "A", "B", "C")
# 打印： A ===> C
# 步骤3： hanota(2, "B", "A", "C")

# 第七次调用： hanota(2, "B", "A", "C")

# 步骤1： hanota(1, "B", "C", "A")

# 第八次调用： hanota(1, "B", "C", "A")
# 打印： B ===> A
# 步骤2： hanota(1, "B", "A", "C")

# 第九次调用： hanota(1, "B", "A", "C")
# 打印： B ===> C
# 步骤3： hanota(1, "A", "B", "C")

# 第十次调用： hanota(1, "A", "B", "C")
# 打印： A ===> C
