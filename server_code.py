import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening for incoming connections...")

# Accept incoming connection
client_socket, client_address = server_socket.accept()
print("Connection established with:", client_address)

# Receive data from client
data = client_socket.recv(1024).decode()

# Firewall Rule: Allow requests starting with "ALLOW:"
if data.startswith("ALLOW:"):
    # Extract the content after "ALLOW:" for further processing
    content = data[len("ALLOW:"):]
    
    # Process the allowed request (simplified)
    response = f"Allowed request content: {content}"
else:
    response = "Request blocked by firewall rule."

# Send the response back to the client
client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
