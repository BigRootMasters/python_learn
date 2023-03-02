# print()函数打印
print("hello world")
print(11)
print(11.2)
print("hello world", "hello python")

# 注释
# 单行注释#
# 多行注释"""   """
# 变量赋值
int_type = 11,
float_type = 11.2,
str_type = "hello python"

# type() 查看变量类型
type(11)
type(int_type)
type(11.2)
type(float_type)
type("hello python")
type(str_type)

# 输出变量类型
print(type(11))
print(type(int_type))
print(type(11.2))
print(type(float_type))
print(type("hello python"))
print(type(str_type))

# 变量类型转换
print(print(str(11)), 11)
print(type(int("11")), type("11"))
print(float("11.2"), "11.2")

# 标识符
# 内容限定 只能使用中文，英文，数字，下划线     不能以数字开头
# 不以关键字命名变量
# python大小写敏感
# 标识符

# 算术运算
# 加
print(1 + 1)
#  减
print(1 - 1)
# 乘法
print(1 * 1)
# 除法
print(2 / 1)
# 取整
print(11 // 2)
# 取余
print(9 % 2)
# 指数
print(2 ** 2)

# 复合运算
print("--------------------------------")
num = 4
# +=
num += 1
print(num)
# -=
num -= 1
print(num)
# *=
num *= 2
print(num)
# /=
num /= 2
print(num)
# %= 取模/取余
num %= 2
print(num)
a = 9
a %= 2
print(a)
# //= 取整
b = 9
b //= 2
print(a)
# **=
a = 9
a **= 2
print(a)

# 字符串
print("--------------------------------")
print(type('li'), type('"99"'))
print(type("li"), type("'9'"), type("\"9\""))
print(type("""li"""))

# 占位符
str1 = "li"
int1 = 11
float1 = 11.21111111
print("wo___%s___%d___%f" % (str1, int1, float1))
print("11限制宽度限制5，%5d" % int1)
print("11限制宽度限制1，%1d" % int1)
print("11.21111111限制宽度限制7,小说精度2，%7.2f" % float1)
print("11.21111111限制宽度限制不限制,小说精度2，%.2f" % float1)

# f格式字符串
name = "li"
money = 11
money_1 = 111.2
print(f"1:{name},2:{money},3:{money_1}")

# input
print("你的名字是?")
you_name = input()
print(you_name)
