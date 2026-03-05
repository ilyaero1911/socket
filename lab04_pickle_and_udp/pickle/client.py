import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(b"hello udp", ('localhost',9091))

data, addr = sock.recvfrom(1024)

print("echo", data.decode())

sock.close()
