# 导入

import time

# from time import sleep

# from time import *


# from time import sleep as sl

# 不同模块的同名功能，后面的会覆盖前面

# main类似于单元测试，在文件内执行时会有

# __all__ = [''] 控制导入的*指定内容


if __name__ == "__main__":
    print("main")


def fun1():
    print("睡前")
    time.sleep(5)
    print("睡后")


fun1()
