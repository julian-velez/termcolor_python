# pip install termcolor
from termcolor import colored
import random

mensaje = "hola julian velez G"
colores = ['cyan', 'red', 'green', 'blue', 'yellow']

# Creamos una lista donde cada letra se colorea con un color aleatorio
texto_coloreado = ""
for letra in mensaje:
    if letra != " ":  # No pintamos los espacios
        color = random.choice(colores)
        texto_coloreado += colored(letra, color)
    else:
        texto_coloreado += " "

print(texto_coloreado)
