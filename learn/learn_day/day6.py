import learn.my_package.module_1
import learn.my_package.module_2

learn.my_package.module_1.module_1()
learn.my_package.module_2.module_2()

from learn.my_package import module_1
from learn.my_package import module_2

module_1.module_1()
module_2.module_2()

from learn.my_package.module_1 import module_1
from learn.my_package.module_2 import module_2

module_1()
module_2()


def reverse_str(s):
    return s[::-1]


str = reverse_str("lkk")
print(str)
