clients = []

clients.append("Alice")
clients.append("Bob")
clients.append("Charlie")

new_client = input("Enter a new client name: ")
clients.append(new_client)

for client in clients:
    print(client)