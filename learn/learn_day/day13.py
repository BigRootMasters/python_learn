"""
私有方法在类内部调用，
class xx(父类)
"""


class NFC:
    __voltage = 0.5

    def __keep(self):
        print("私有")

    def call(self):
        if self.__voltage >= 1:
            print("5G")
        else:
            self.__keep()
            print("4G")


class Red:
    __voltage = 0.5

    def __keep(self):
        print("私有")

    def red_f(self):
        print("red")


class Phone(NFC, Red):
    imei = "phone"

    def say(self):
        print("new_func")


class MyPhone(Phone):
    # 完善类结构，无具体功能
    pass
    imei = "myPhone"

    def say(self):
        # 调用父类方法
        Phone.say(self)
        # 调用父类方法
        super().say()
        print("myPhone")


nfc = NFC()
nfc.call()

phone = Phone()
phone.say()

my = MyPhone()
my.say()
