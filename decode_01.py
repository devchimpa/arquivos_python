#!/bin/python3

frase_decodificada = base64.b64decode(frase_encriptada).decode("utf-8")
  print(frase_decodificada)

  #Complemento ao código encode
