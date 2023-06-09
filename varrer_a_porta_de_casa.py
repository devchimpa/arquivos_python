#!/usr/bin/Python3
import socket

alvo=input("Alvo: ")
portas= [ 22, 80, 8080, 443, 21]
for porta in portas:
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	resultado= sock.connect_ex((alvo,porta))
	sock.close()
	if (resultado ==0):
		print("Porta aberta: ",porta)
