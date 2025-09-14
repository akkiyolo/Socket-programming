import sys
import socket

# Create a TCP socket for IPv4 communication
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET for IPv4, SOCK_STREAM for TCP
    print("socket created succesfully")
except socket.error as err:
    print(f"socket creattion failed with error {err}")  # Handle socket creation errors
    sys.exit()  # Exit if socket creation fails

# Define the port to connect to (80 for HTTP)
port = 80

# Resolve the hostname 'www.github.com' to an IP address via DNS
try:
    host_ip = socket.gethostbyname('www.github.com')  # Converts hostname to IP (e.g., 140.82.113.4)
except socket.gaierror:  # Handle DNS resolution errors (e.g., invalid hostname or no DNS response)
    print("error resolving the host")
    sys.exit()  # Exit if DNS resolution fails

# Connect to GitHub's server using the resolved IP and port
s.connect((host_ip, port))  # Establishes a TCP connection to the server
print(f"socket has successfully connected to github on port == {host_ip}")  # Print confirmation (note: should likely show port number)

# Note: Socket should be closed after use to free resources
s.close()  # Close the socket connection