class MyClass:
    mutable_class_attr = []  # 可变类型
    immutable_class_attr = "I am immutable"

    def __init__(self, name):
        self.instance_attr = name


# 创建实例
class1 = MyClass("Instance 1")
class2 = MyClass("Instance 2")

# 修改可变类型的类属性
class1.mutable_class_attr.append("Modified by class1")
print(MyClass.mutable_class_attr)  # 输出: ['Modified by class1']
print(class2.mutable_class_attr)  # 输出: ['Modified by class1']

# 修改不可变类型的类属性
class1.immutable_class_attr = "Modified by class1"
print(MyClass.immutable_class_attr)  # 输出: I am immutable
print(class2.immutable_class_attr)  # 输出: I am immutable
print(class1.immutable_class_attr)  # 输出: Modified by class1
