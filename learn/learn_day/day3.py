# 异常

def fun_1():
    print("fun1")
    i = 1 / 0


def fun_2():
    fun_1()


def fun_3():
    try:
        fun_2()
        return True
    except Exception:
        print("exception")
        return False
    finally:
        print("done")
        return False


r = fun_3()
print(r)
