import socket

HOST = "127.0.0.1"   # Localhost
PORT = 5000          # Port number

# Create the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server.bind((HOST, PORT))

# Listen for incoming connections
server.listen()

print("Server is running...")
print("Waiting for client to connect...")

# Accept a client connection
conn, addr = server.accept()
print("Connected by:", addr)

# Receive data from the client
data = conn.recv(1024)

# Decode and display the message
message = data.decode()
print("Client says:", message)

# Send a response back to the client
response = "Server received: " + message
conn.send(response.encode())

# Close the connection
conn.close()
server.close()