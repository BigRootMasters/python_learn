"""
递归
"""

import os


def test_os():
    print(os.listdir("/Users/kuan/Desktop"))
    print(os.path.isdir("/Users/kuan/Desktop"))
    print(os.path.exists("/Users/kuan/Desktop"))


if __name__ == '__main__':
    test_os()