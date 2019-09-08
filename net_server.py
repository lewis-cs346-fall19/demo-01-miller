import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('0.0.0.0', 47874)
s.bind(addr)
s.listen(5)
(connectedSock, clientAddress) = s.accept()
msg = "xxxx"
while msg != "quit":
    try:
        msg = connectedSock.recv(1024).decode()
        print("data = ", msg)
        connectedSock.sendall(msg.encode())
    except ConnectionAbortedError:
        connectedSock.close()
