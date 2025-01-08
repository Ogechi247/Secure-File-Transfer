import socket

def udp_broadcast():
    # Prompt the client user for their name and port number
    name = input("Enter your name: ")
    port = int(input("Enter the port number to send the broadcast to: "))

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Broadcast a message to the server
    message = f"Hello {name}, I'm B, nice to meet you".encode()
    client.sendto(message, ("<broadcast>", port))
    print("Broadcast sent.")

    # Wait for a response from the server
    data, addr = client.recvfrom(1024)
    print(f"Received response: {data.decode()}")

# Send a UDP broadcast
udp_broadcast()
