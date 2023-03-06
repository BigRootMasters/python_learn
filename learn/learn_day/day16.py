"""
装饰器

闭包时传入方法
"""


# 方式1
# def outer(func):
#     def inner():
#         print('睡')
#         func()
#         print('起')
# 
#     return inner
#
#
# def sleep():
#     import random
#     import time
#     print('sleep')
#     time.sleep(random.randint(1, 5))
#
#
# fn = outer(sleep)
# fn()


# 方式2
def outer(func):
    def inner():
        print('睡')
        func()
        print('起')

    return inner


@outer
def sleep():
    import random
    import time
    print('sleep')
    time.sleep(random.randint(1, 5))


sleep()
