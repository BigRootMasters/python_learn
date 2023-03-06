# test
flag = 11 < 9

print(f"flag{flag},{type(flag)}")

if flag:
    print("1")
# elif not flag:
#     print("2")
else:
    print("3")
print("4")

i = 0
while i < 5:
    print("88")
    i += 1

str = '887883'
for x in str:
    print(x)


def test1(r):
    print(r)
    test2()


def test2():
    print(11)


test1("999")

num = 100


def fun_1(r):
    print(r)
    fun_2()


def fun_2():
    global num
    num += 1
    print(num)


fun_1(num)
print(num)



