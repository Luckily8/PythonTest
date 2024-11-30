# 功能不必硬记住，只要知道有这个功能，以后遇到了再查就行了
# f格式化的作用就是让{}被识别为占位符
mylist = [0, 1, 2, 3, 4]
# list_1 = mylist.index(1)
# print(f"1在列表中的位置是：{list_1}")
print(mylist)
# list元素的追加
# mylist.append(5)
# print(mylist)
# mylist.append([6,7])
# print(f"append追加[6,7]:{mylist}")
# mylist.extend(["8","9"])
# print(f"extend追加[8,9]:{mylist}")

# 列表元素的删除:无返回值-remove(元素),从前往后搜索第一个匹配元素
# # 有返回值=pop(位置),
# del mylist[4]
# del_save = mylist.remove(1)
# print(f"remove删除1:{mylist},返回值是:{del_save}")
# del_save = mylist.pop(1)
# print(f"pop删除1:{mylist},返回值是:{del_save}")

# # 增删查改,len(list)
# # # list元素的追加
# mylist.append(5)

# # # list元素的插入
# mylist.insert(2,1)

# # # list元素的查找
# list_1 = mylist.index(1)
# print(f"1在列表中的位置是：{list_1}")

# # # list元素的修改
# mylist[1] = 10
# print(f"修改第1个元素为10:{mylist}")

# 列表的遍历,whie和for的区别在于for可以直接遍历元素，而while需要索引
# for i in mylist: # lise赋值给i
#     print(i)
# while mylist:  # 在 while 循环中，条件是 mylist，这意味着只要 mylist 不为空，循环就会继续执行
#     print(mylist.pop(0))
# 需要注意的是，pop(0) 方法在移除列表第一个元素时，会导致列表中的其他元素向前移动，这在大列表中可能会导致性能问题。如果你需要频繁地从列表中移除第一个元素，
# 使用 collections.deque 可能会更高效，因为 deque 的 popleft 方法在时间复杂度上是 O(1)。

# 实战 去除列表内的偶数
i = 0
list_oushu = []
while i < len(mylist):
    if mylist[i] % 2 == 0:
        list_oushu.append(mylist[i])
    i += 1
print(f"偶数列表:{list_oushu},原列表:{mylist}")

# 官方文档 weapon是一个字符串，strip()方法去除字符串两边的空格
# call a method on each element
freshfruit = ["  banana", "  loganberry ", "passion fruit  "]
[weapon.strip() for weapon in freshfruit]

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[
    num for elem in vec for num in elem
]  # for elem in vec获得一维列表，for num in elem获得元素
