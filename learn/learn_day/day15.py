"""
闭包
返回值时调用内部方法

"""


def func(out):
    def sugar(inter):
        # nonlocal 修改外部变量时需要修饰
        print(out, inter)

    return sugar


f1 = func("88")
f1("inter")
