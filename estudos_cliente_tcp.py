#!/usr/bin/python3

from socket import *

servidor = "192.168.1.2"
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor, porta))

while True:
    msg = input("Digite sua mensagem: ")

    if not msg:
        break

    obj_socket.send(bytes(msg, 'utf-8'))
    resposta = obj_socket.recv(1024)
    print("Recebido:", resposta.decode())

obj_socket.close()

