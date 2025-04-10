import time
import sys
import threading as thr
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
    detener = False  #Variable de control que detiene el bucle

    def esperar_input():
        nonlocal detener #modificamos la variable externa y la hacemos interna con nonlocal
        input(" Presiona Enter para Salir ")
        detener = True #Cambia la variable detener a True para detener el efecto de mecanografia
    
    hilo = thr.Thread(target=esperar_input) #Crea un hilo para esperar la entrada del usuario
    hilo.start() #Inicia el hilo
    """ Nota mental : No se puede usar el hilo en la funcion principal porque el hilo no se detiene y el programa no termina
    se queda esperando la entrada del usuario y el hilo no se detiene
    por eso se usa un bucle while para esperar la entrada del usuario y el hilo se detiene cuando se recibe la entrada
    """
    #Ultima nota mental , los hilos segun su uso estan bastante rotos ( son muy utiles o muy buenos al uso practico)
    while not detener:
        for letra in texto:
            if detener:
                break
            sys.stdout.write(letra) #Escribe la letra en la consola
            sys.stdout.flush()
            time.sleep(0.1) #Espera 0.1 segundos antes de escribir la siguiente letra
        sys.stdout.write("\n") #Regresa el cursor al inicio de la linea
        sys.stdout.flush()
        time.sleep(1)
mecanografiaBucle("......")