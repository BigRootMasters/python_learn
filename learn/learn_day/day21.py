"""
socket客户端
"""

import socket

socket_client = socket.socket()
socket_client.connect(('localhost', 8000))
while True:
    input_send = input()
    if input_send == "exit":
        break
    #  客户端发送数据
    socket_client.send(input_send.encode("utf-8"))
    # 服务端返回数据
    send_data = socket_client.recv(1024)
    print(send_data.decode("utf-8"))
socket_client.close()
