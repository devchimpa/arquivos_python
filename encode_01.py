#!/bin/python3

import base64

frase=input("Digite a frase: ")
frase_codificada = base64.b64encode(frase.encode("utf-8"))

print(frase_codificada)
