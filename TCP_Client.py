import socket
import ssl
import os

# File paths based on my actual filenames
client_cert = 'Jason_cert.pem'
client_key = 'private.pem'
ca_cert = 'ca_cert.pem'

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create an SSL context
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_cert_chain(certfile=client_cert, keyfile=client_key)
context.load_verify_locations(cafile=ca_cert)
context.verify_mode = ssl.CERT_OPTIONAL

# Connect to the server 
port = int(input("Enter the port number to use for communication: "))

try:
    client_socket.connect(('localhost', port))
    # Wrap the socket with SSL
    ssl_client_socket = context.wrap_socket(client_socket, server_hostname='localhost')

    # Send the file
    file_path = input("Enter the path of the file to send: ")
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
    else:
        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(1024):
                    ssl_client_socket.send(chunk)
            print("File sent successfully.")
        except Exception as e:
            print(f"Error while sending the file: {e}")
finally:
    # Close the connection
    ssl_client_socket.close()
    print("Connection closed.")
