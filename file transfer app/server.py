# server.py
import socket
import os

# Define host and port
HOST = '0.0.0.0'   # listens on all interfaces
PORT = 5001        # can be any unused port

# Create socket
server = socket.socket()
server.bind((HOST, PORT))
server.listen(5)
print(f"[+] Server started, listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"[+] Connected to {addr}")

# Receive file info
filename = conn.recv(1024).decode()
if not filename:
    print("[-] No filename received")
    conn.close()
    exit()

file_size = int(conn.recv(1024).decode())
print(f"[+] Receiving '{filename}' ({file_size} bytes)")

# Receive the actual file
with open(filename, "wb") as f:
    bytes_received = 0
    while bytes_received < file_size:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)
        bytes_received += len(data)

print(f"[+] File '{filename}' received successfully.")
conn.close()
server.close()
