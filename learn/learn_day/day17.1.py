"""
单例模式
每次类的结果不一样
"""


class Tool:
    pass


str_tool = Tool()

t1 = Tool()
t2 = Tool()
print(t1)
print(t2)
print(id(t1), id(t2))
print(t1 == t2)
s1 = str_tool
s2 = str_tool
print(s1 == s2)
print(s1)
print(s2)
