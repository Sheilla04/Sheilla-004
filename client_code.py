import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Send an allowed request to the server
allowed_request = "ALLOW:This is an allowed request."
allowed_request = "ALLOW:Hello, Server! This is a client request."
client_socket.send(allowed_request.encode())

# Receive the response from the server
response = client_socket.recv(1024).decode()
print("Server response:", response)

# Close the connection
client_socket.close()
