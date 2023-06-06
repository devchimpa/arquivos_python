#!/usr/bin/python3
from socket import *

servidor = "192.168.1.2"
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor, porta))
obj_socket.listen(2)

print("Aguardando conexão...")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com:", cliente)

    while True:
        msg_recebida = con.recv(1024).decode()
        print("Recebido:", msg_recebida)

        if not msg_recebida:
            break

        msg_entrada = input("Digite a resposta: ")

        if not msg_entrada:
            break

        con.send(msg_entrada.encode())

    con.close()
