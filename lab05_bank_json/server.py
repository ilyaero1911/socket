import socket
import json


class Bank:

    def __init__(self, initial=0):
        self.balance = initial

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return None


PORT = 9092

bank = Bank()

sock = socket.socket()
sock.bind(('', PORT))
sock.listen(1)

print("Bank server on port", PORT)

conn, addr = sock.accept()
print("client", addr)

data = conn.recv(1024).decode()

request = json.loads(data)

action = request.get("action")

if action == "balance":

    reply = {
        "ok": True,
        "balance": bank.get_balance()
    }

elif action == "deposit":

    amount = request.get("amount", 0)

    new_balance = bank.deposit(amount)

    reply = {
        "ok": True,
        "balance": new_balance
    }

elif action == "withdraw":

    amount = request.get("amount", 0)

    new_balance = bank.withdraw(amount)

    if new_balance is None:

        reply = {
            "ok": False,
            "error": "insufficient funds",
            "balance": bank.get_balance()
        }

    else:

        reply = {
            "ok": True,
            "balance": new_balance
        }

else:

    reply = {
        "ok": False,
        "error": "unknown action"
    }

conn.send(json.dumps(reply).encode())

conn.close()
sock.close()
