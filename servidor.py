#Laura Sanz Ruano G.ITT

#! /usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Nos libera automaticamente el puerto para poder reutilizarlo
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        IP = address[0]
        Puerto = address[1]
        print 'HTTP request received:'
        print recvSocket.recv(1024)

        numero = random.randint(0, 100)

        html = "<html><body><h1>"+"Hola!, World!<h1><p> And in particular hello to you, " + str(Puerto)
        html+= '<p><a href = "http://localhost:1234/' + str(numero) + '">Dame otra</a></p>'
        html+= "</body></html>"
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                       html +
                       "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Servidor interrumpido"
    mySocket.close()
