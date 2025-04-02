import socket

# Server settings
HOST = "0.0.0.0"  # Accept connections on all available interfaces
PORT = 65432       # Port number (make sure it's not blocked by firewall)

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Listen for 1 connection at a time
print(f"🚀 Server listening on {HOST}:{PORT}")

# Accept client connection
conn, addr = server_socket.accept()
print(f"✅ Connected by {addr}")

# Receive data
data = conn.recv(1024).decode()
print(f"📩 Received data: {data}")

# Close connection
conn.close()
server_socket.close()
