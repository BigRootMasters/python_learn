"""
类的基础
self 表示类自身，方法内部访问
"""


class Student:
    name = None
    age = None
    gender = None

    def say(self):
        print(self.name)

    def helio(self,msg):
        print(self.name,msg)


stud_1 = Student()
stud_1.name = "John"
stud_1.age = 20
stud_1.gender = "Male"
stud_1.say()
stud_1.helio("biu,biu,biu")
# print(stud_1.name)
