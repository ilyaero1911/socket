import socket
import pickle

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

conn, addr = sock.accept()

data = conn.recv(4096)

conn.send(data)

conn.close()
sock.close()
