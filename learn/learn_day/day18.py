"""
工厂模式
"""


class Person():
    pass


class Worker():
    pass


class Student():
    pass


class Teacher():
    pass


class PersonFactory():
    def getPerson(self, p_type):
        if p_type == 'person':
            return Person()
        elif p_type == 'worker':
            return Worker()
        elif p_type == 'student':
            return Student()
        elif p_type == 'teacher':
            return Teacher()
        else:
            return None


pf = PersonFactory()
p = pf.getPerson("person")
stu = pf.getPerson("student")
worker = pf.getPerson("worker")
