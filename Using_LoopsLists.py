clients = []
new_client = ""
while new_client != "exit":
    new_client = input("Enter a new client name: ")
if new_client != "exit":
    clients.append(new_client)


print("The clients are:")
for client in clients:
    print(f" {client}")