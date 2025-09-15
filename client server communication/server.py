## server uses a bind() method so that it can listen to request coming up from a specific port

## other is listen() this helps server to listen to the requets coming up from a particular client

## accept() initiates a connection with the client
 
## close() closes the connection with the client

import socket

s=socket.socket()
print('socket created')

port= 56789

s.bind(('',port))
print(f'socket binded to {port}')

s.listen(5)
print('socket is listening')

while True:
  c,addr=s.accept()
  print('got connection form',addr)
  message=('Thank you for connecting')
  c.send(message.encode())
  c.close()