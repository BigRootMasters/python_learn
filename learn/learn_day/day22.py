"""
正则
"""

import re

s = "hello world"

o = re.match("hello", s)
print(o)
print(o.group)
print(o.start)
print(o.span)
