import time
import sys

def mecanografiar(texto):
    """La funcion recibe un  argumento , el texto que quieras mecanografiar(que  debe ser una cadena)"""
    lista = texto.split() #Separa el texto en una lista de palabras
    for palabra in lista:
        sys.stdout.write(palabra + " ") #Escribe la palabra en la consola
        sys.stdout.flush() #Asegura que el texto se imprima inmediatamente
        time.sleep(0.4) #Espera 0.4 segundos antes de escribir la siguiente palabra

mecanografiar("Hola, soy un texto mecanografiado :D")
print(" ")

