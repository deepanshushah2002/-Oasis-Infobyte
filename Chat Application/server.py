import socket
import threading


# Function to handle client connections
def handle_client(client_socket, client_address):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break
        print(f"Received message from {client_address}: {data}")

        # Broadcast the received message to all clients
        for c in clients:
            if c != client_socket:
                c.send(data.encode("utf-8"))

    # Remove the client from the list
    clients.remove(client_socket)
    client_socket.close()


# Server configuration
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5555))
server.listen(5)

print("Server is running...")

clients = []

while True:
    client_socket, client_address = server.accept()
    print(f"Connection from {client_address} established.")

    clients.append(client_socket)

    # Start a new thread for each connected client
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket, client_address)
    )
    client_thread.start()
