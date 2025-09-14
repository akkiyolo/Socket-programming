import sys
import socket


try:
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  print("socket created succesfully")
except socket.error as err:
  print(f"socket creattion failed with error {err}")

port=80

try :
  host_ip=socket.gethostbyname('www.github.com')
except socket.gaierror: ## gaierror simplies means that there might be some problem with the dns
  print("error resolving the host")
  sys.exit()

s.connect((host_ip,port))
print(f"socket has successfully connected to github on port == {host_ip}")

