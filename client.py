import socket

HOST = "127.0.0.1"   # Localhost
PORT = 5000          # Same port as the server

# Create the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((HOST, PORT))

# Ask the user for a message
message = input("Enter a message for the server: ")

# Send the message
client.send(message.encode())

# Receive the server's response
response = client.recv(1024)

# Display the response
print("Server replied:", response.decode())

# Close the connection
client.close()