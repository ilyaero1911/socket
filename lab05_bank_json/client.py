import socket
import json

action = input("Action (balance / deposit / withdraw): ").strip().lower()

request = {"action": action}

if action == "deposit" or action == "withdraw":

    amount = int(input("Amount: "))

    request["amount"] = amount

sock = socket.socket()

sock.connect(('localhost', 9092))

sock.send(json.dumps(request).encode())

data = sock.recv(1024).decode()

sock.close()

reply = json.loads(data)

if reply.get("ok"):

    print("Balance:", reply["balance"])

else:

    print("Error:", reply.get("error"))
