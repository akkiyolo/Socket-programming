'''Socket Programming'''
# Sockets are endpoints for communication between devices over a network, allowing programs to send and receive data.

## TCP sockets provide reliable, connection-oriented communication (e.g., for web servers using HTTP).
## UDP sockets are connectionless and faster but less reliable (e.g., for streaming or gaming).

## server sockets listens to port at IP and client sockets connects to server

import socket
import sys

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

## AF_INET refers to network family that is IPv4
## SOCK_STREAM connection orientted TCP protocol

## We can using the command that is ping to know what is the ip address of a particular domain name 

## ping www.gopogle.com

ip= socket.gethostbyname('www.github.com')

print(ip)