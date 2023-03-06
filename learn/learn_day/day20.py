"""
socket服务端
"""

import socket

socket_server = socket.socket()
socket_server.bind(('localhost', 8000))
# 允许的链接数量
socket_server.listen(1)

# result: tuple = socket_server.accept()
# con = result[0]hi

# address =ult[1]
con, add = socket_server.accept()

# accept 阻塞方法,如果没连接则一直等待
while True:
    data = con.recv(1024).decode('utf8')
    print(data)
    msg = input("输入信息")
    if msg == "exit":
        break
    con.send(msg.encode('utf8'))
con.close()
socket_server.close()
