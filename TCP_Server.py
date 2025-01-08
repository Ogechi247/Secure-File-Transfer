import socket
import ssl
import os
import random

# File paths based on my actual filenames
server_cert = 'oge_cert.pem'
server_key = 'private.pem'
ca_cert = 'ca_cert.pem'

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to a random port
port = random.randint(1024, 65535)
server_socket.bind(('0.0.0.0', port))
server_socket.listen(1)

# Create an SSL context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
passphrase = input("Enter PEM pass phrase: ")
context.load_cert_chain(certfile=server_cert, keyfile=server_key, password=passphrase)
context.load_verify_locations(cafile=ca_cert)
context.verify_mode = ssl.CERT_OPTIONAL

print(f"Server listening for connections on port {port}...")

# Accept incoming connection
connection, address = server_socket.accept()
print("Client connected:", address)

# Wrap the connection with SSL
ssl_connection = context.wrap_socket(connection, server_side=True)

# Receive the file
with open("received_file", "wb") as f:
    while True:
        data = ssl_connection.recv(1024)
        if not data:
            break
        f.write(data)
print("File received successfully.")

# Close the connection
ssl_connection.close()
server_socket.close()
