"""
闹钟
"""


class Clock:
    name = None

    def  ring(self):
        import winsound
        winsound.Beep(2000, 1000)


clock = Clock()
clock.ring()
