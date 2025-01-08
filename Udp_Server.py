import socket

def udp_server():
    # Prompt the server user for a port number and name
    port = int(input("Enter the port number to listen on: "))
    name = input("Who are you? ")

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("0.0.0.0", port))

    print(f"Listening for broadcasts on port {port}...")

    while True:
        data, addr = server.recvfrom(1024)
        message = data.decode()
        print(f"Received from {addr}: {message}")
        if message.startswith("Hello"):
            print(f"Hello {name}, nice to meet you!")
            # Respond with a greeting message
            server.sendto(f"Hello {name}, nice to meet you!".encode(), addr)

# Run the UDP server
udp_server()
