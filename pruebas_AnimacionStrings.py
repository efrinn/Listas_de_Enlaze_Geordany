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

def mecanografiar2(texto):
    """La funcion recibe el texto en el que deseas hacer el efecto"""
    for letra in texto:
        sys.stdout.write(letra) #Escribe la letra en la consola
        sys.stdout.flush() #Asegura que el texto se imprima inmediatamente
        time.sleep(0.1) #Espera 0.1 segundos antes de escribir la siguiente letra

mecanografiar2("Saliendo ....")

def mecanografiaBucle(texto):
    """Hacer un bucle de efecto de maquina de escribir"""
    while True:
        for letra in texto:
            sys.stdout.write(letra) #Escribe la letra en la consola
            sys.stdout.flush()
            time.sleep(0.1) #Espera 0.1 segundos antes de escribir la siguiente letra
        sys.stdout.write("\n") #Regresa el cursor al inicio de la linea
        sys.stdout.flush()
        time.sleep(1)
mecanografiaBucle("......")