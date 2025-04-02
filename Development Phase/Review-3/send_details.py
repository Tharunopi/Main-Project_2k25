import socket

# Server details
HOST = "0.0.0.0"  # Accept connections from any IP
PORT = 65432       # Use a free port (ensure it's open in your firewall)

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"🚀 Server listening on {HOST}:{PORT}")

# Accept client connection
conn, addr = server_socket.accept()
print(f"✅ Connected by {addr}")

# Receive data
data = conn.recv(1024).decode()
print(f"📩 Received: {data}")

# Close connection
conn.close()
server_socket.close()
