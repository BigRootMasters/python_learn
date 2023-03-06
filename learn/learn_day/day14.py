# 类型注解


from typing import Union


# x,y为参数注解，int为返回类型
def add(x: int, y: int) -> int:
    return x + y


s = add(1, 2)
print(s)

"""
Union 联合类型注解
"""

my_list: list[Union[int, str]] = [1, 2, "it", "te"]


def func(data: Union[int, str]) -> Union[int, str]:
    pass


func()
