import os
#Fatorial de un numero


def pause():
    input("Presione enter para continuar...")

def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def factorial(num):
    if num == 0:
        return 1
    else :
        return num * factorial(num -1)
    
#ejemplo de uso 
numero = 6
resultado = factorial(numero)

print(resultado)

def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num -2)

fib = fibonacci(numero)
for i in range (numero + 1):
    print(fibonacci(i) , end='')

pause()
limpiarPantalla()

listaFact = []
listaFibonacci = []

#Cargar numeros en la lista
def cargarFact(num):
    for i in range (1 ,num +1):
        listaFact.append(factorial(i))
    return listaFact
def cargarFibonacci(num):
    for i in range (1, num +1 ):
        listaFibonacci.append(fibonacci(i))
    return listaFibonacci

class SerieFact:
    def __init__(self , numero = None , nodo = None):
        self.numero = numero
        self.nodo = nodo
    
    def __str__(self):
        return str(self.numero)

class SerieFib:
    def __init__(self , numero = None , nodo = None):
        self.numero = numero
        self.nodo = nodo
    def __str__(self):
        return str(self.numero)

numeros = int(input("Ingrese el o los numeros: "))
print(f"Este es el factorial del numero {numeros} = {cargarFact(numeros)}")

print(f"Esta es la sucesion de fibonbacci del numero {numeros} contada de atras para adelante = {cargarFibonacci(numeros)}")



def main():
    numero = int(input("Ingresa un numero: "))



    for i in range (1,numero + 1):
        sfi = SerieFib(i, fibonacci(i))
        listaFibonacci.append(sfi)
        sf = SerieFact(i , factorial(i))
        listaFact.append(sf)
    
    print("Facotorial: ")
    for i in listaFact:
        print(i)
    print("Fibonacci: ")
    