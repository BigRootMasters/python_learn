"""
数据容器
"""
# 列表
my_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# 元组
my_tuple = ("1", "2", "3", "4", "5", "6", "7", "8")
# 字符串
my_string = "123456"
# 集合
my_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
# 字典
my_dict = {"1": "1", "2": "2", "3": "3", "4": "4"}


# 方法参数
def ob(age, name, gender):
    print(age, name, gender)


# 位置参数
ob("age", "name", "gender")
# 关键字参数
ob(name="name", gender="male", age="age")


# 默认传参数/缺省参数
def add(age, name, gender="男"):
    print(age, name, gender)


add("name", "age")


# 不定长
def arg(*args):
    print(args)
    return 1, 2


x, y = arg("不定长1", "2", "3")
print(x, y)


# 关键字不定长
def kwarg(**kwargs):
    print(kwargs)


kwarg(name="name", age=3)

