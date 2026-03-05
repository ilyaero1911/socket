import socket

sock = socket.socket()

sock.connect(('localhost', 9090))

while True:

    msg = input("message: ")

    sock.send(msg.encode())

    if msg == "exit":
        break

    data = sock.recv(1024)

    print("echo:", data.decode())

sock.close()
