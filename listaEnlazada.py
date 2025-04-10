import datetime as dt
import os

def pause():
    input("Presione enter para continuar...")

def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class Solicitud:
    def __init__(self , nombre , asunto , carrera , siguiente = None):
        self.nombre = nombre
        self.fecha = dt.date.today()
        self.asunto = asunto
        self.carrera = carrera
        self.siguiente = siguiente
    
    def __str__(self):
        return f"Estudiante: {self.nombre} , Asunto: {self.asunto} , Carrera: {self.carrera} ->"
    
lista_solicitudes = []    
def agregar_solicitud(nombre , asunto , carrera):
    nueva_solicitud = Solicitud(nombre , asunto , carrera)
    lista_solicitudes.append(nueva_solicitud)
    return nueva_solicitud

def mostrar_solicitudes():
    for solicitud in lista_solicitudes:
        print(solicitud)

def main():
    while True:
        limpiarPantalla()
        print("1. Agregar Solicitud")
        print("2. Mostrar Solicitudes")
        print("3. Salir")
        
        opcion = input("Seleccione una opcion: ")
            
        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            asunto = input("Ingrese el asunto de la solicitud: ")
            carrera = input("Ingrese la carrera del estudiante: ")
            agregar_solicitud(nombre , asunto , carrera)
            print(f"Solicitud de {nombre} agregada con exito!")
            pause()
        elif opcion == "2":
            mostrar_solicitudes()
            pause()
        elif opcion == "3":
            print("Saliendo...")
            pause()
            limpiarPantalla()
            break
        else:
            print("Opcion no valida!")
            pause()

if __name__ == "__main__":
    main()