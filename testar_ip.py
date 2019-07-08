#!/usr/bin/python
import socket 
ip = raw_input("entre com o endereco do IP: ")
port = input(" entre com o numero do porta: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if sock.connect_ex((ip,port)):
    print " deu ruim", port, "esta fechada"
else:
    print "a porta", port "esta aberta"    