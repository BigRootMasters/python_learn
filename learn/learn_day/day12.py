"""
构造方法
__init__ 创造类或对象时自动执行，传入参数哦自动传递给__init__
"""


class Student(object):
    name = None
    age = None

    # 私有成员变量 __
    __address = None

    # 私有成员方法
    def __address_func(self):
        print(self.__address)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 控制类转字符串输出
    def __str__(self):
        return 'name: %s, age: %s' % (self.name, self.age)

    def __repr__(self):
        return 'name: %s, age: %s' % (self.name, self.age)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):
        return self.name != other.name or self.age != other.age

    # 小于
    def __lt__(self, other):
        return self.age < other.age

    #     小于等于
    def __le__(self, other):
        return self.age <= other.age

    # 大于
    def __gt__(self, other):
        return self.age > other.age


stu = Student("周劼", "3")
stu2 = Student("周劼", "4")
print(stu)
print(stu.name, stu.age)
print(stu == stu2)
print(stu.__lt__(stu2))
print(stu.__le__(stu2))
print(stu.__gt__(stu2))


