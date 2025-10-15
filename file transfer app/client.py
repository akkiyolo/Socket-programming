# client.py
import socket
import os

# Define server details
SERVER_HOST = '127.0.0.1'  # change this to server IP if remote
SERVER_PORT = 5001

# Create socket
client = socket.socket()
client.connect((SERVER_HOST, SERVER_PORT))
print(f"[+] Connected to {SERVER_HOST}:{SERVER_PORT}")

# Choose file to send
filename = input("Enter file path: ")
if not os.path.exists(filename):
    print("[-] File not found!")
    client.close()
    exit()

file_size = os.path.getsize(filename)

# Send filename and filesize
client.send(filename.encode())
client.send(str(file_size).encode())

# Send file data
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(1024)
        if not bytes_read:
            break
        client.sendall(bytes_read)

print(f"[+] File '{filename}' sent successfully.")
client.close()
