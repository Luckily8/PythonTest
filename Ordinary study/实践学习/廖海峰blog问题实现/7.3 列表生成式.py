# if写在for前面必须加else，否则报错：
# 这是因为for前面的部分是一个表达式，它必须根据x计算出一个结果

"""
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
使用内建的isinstance函数可以判断一个变量是不是字符串：
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：并全小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = ???
"""
L1 = ["Hello", "World", 18, "Apple", None]
L2 = [i.lower() for i in L1 if isinstance(i, str)]

# 测试:
print(L2)
if L2 == ["hello", "world", "apple"]:
    print("测试通过!")
else:
    print("测试失败!")
