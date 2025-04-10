import os

def pause():
    input("Presione enter para continuar...")

def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class Nodo:
    """Representa un nodo de una lista ligada."""
    def __init__(self , dato):
        self.dato = dato #Aqui se almacenara el valor del nodo
        self.siguiente = None #Apunta hacia el siguiente nodo de la lista , Inicialmente siempre es None
    
class ListaLigada:
    """Aca se crea la lista ligada definiendola como clase"""
    def __init__ (self):
        self.cabeza = None #Primer nodo de la lista ligada 
    
    def insertarNuevoNodo(self , dato):
        """Inserta un nuevo nodo al final de la lista ligada."""
        nuevoNodo = Nodo(dato)
        if self.cabeza is None: #Si la lista esta vacia o si la cabeza es None , el nuevo nodo sera la cabeza
            self.cabeza = nuevoNodo
            return
        actual = self.cabeza
        while actual.siguiente: #Recorre la lista hasta el final
            actual = actual.siguiente
        actual.siguiente = nuevoNodo #El siguiente nodo del nodo actual sera el nuevo nodo
    
    def mostrarNodos(self):
        """Muestra los nodos de la lista ligada."""
        actual = self.cabeza
        while actual:
            print(actual.dato , end=" --> ")
            actual = actual.siguiente
        print("None") #Muestra el fin de la clase ListaLigada
        #El fin de la lista ligada es None
    
    def navegarNodos(self):
        """Navegar en la lista nodo por nodo"""
        actual = self.cabeza
        while actual:
            input(f"Presione enter para pasar a ver el siguiente nodo: {actual.dato}")
            actual = actual.siguiente
        print("Fin de la lista")
        #El fin de la lista ligada es None

    def eliminarNodos(self , dato):
        """Elimina un nodo con el dato ingresado o espesificado"""
        actual = self.cabeza
        #Si el nodo a eliminar es la cabeza 
        #Se verifica si la cabeza es None o si el dato a eliminar es igual al dato de la cabeza
        if actual and actual.dato == dato:
            self.cabeza = actual.siguiente #Si el nodo o dato a eliminar es la cabeza , se cambia la cabeza al siguiente nodo
            actual = None         #El nodo actual se vuelve None para eliminarlo de la memoria
            return
        anterior = None       #Nodo anterior al nodo actual
        #Recorre la lista hasta encontrar el nodo a eliminar
        while actual and actual.dato != dato:
            anterior = actual     #Guarda el nodo actual en el nodo anterior
            actual = actual.siguiente  #Avanza al siguiente nodo
        #Si el nodo a eliminar no existe en la lista
            if not actual:
                return
        anterior.siguiente = actual.siguiente  #El nodo anterior apunta al siguiente nodo del nodo actual
        actual = None #El nodo actual se vuelve None para eliminarlo de la memoria

def main():
    lista = ListaLigada()
    while True:
        limpiarPantalla()
        print("========================================")
        print("██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗  ")   
        print("██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗ ")    
        print("██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║ ")
        print("██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║   ")
        print("██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝    ")
        print("╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝    ")                                                                                
        print("****************************************")
        print("1. Insertar nuevo nodo")
        print("2. Mostrar nodos")
        print("3. Eliminar nodo")
        print("4. Navegar nodo por nodo :D ")
        print("5. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        
        if opcion == "1":
            dato = input("Ingrese el dato del nuevo nodo: ")
            lista.insertarNuevoNodo(dato)
            print(f"Nodo {dato} insertado con exito!")
            pause()
        elif opcion == "2":
            print("Lista de nodos:")
            lista.mostrarNodos()
            pause()
        elif opcion == "3":
            dato = input("Ingrese el dato del nodo a eliminar: ")
            lista.eliminarNodos(dato)
            print(f"Nodo {dato} eliminado con exito!")
            pause()
        elif opcion == "4":
            print("Navegando en los nodos -.- ...:")
            lista.navegarNodos()
            pause()
        elif opcion == "5":
            print("Saliendo...")
            pause()
            limpiarPantalla()
            break
        else:
            print("Opcion no valida!")
            pause()
            limpiarPantalla()
if __name__ == "__main__":
    main()