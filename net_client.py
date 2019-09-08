import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('0.0.0.0', 47874))
    msg = "xxxxxx"
    while msg != "quit":  
        msg = input("Input Message: ")
        s.sendall(msg.encode())
        data = s.recv(1024).decode()
        print("received ", data)
print("ended")
