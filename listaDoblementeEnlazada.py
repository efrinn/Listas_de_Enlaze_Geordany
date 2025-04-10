import os

def pause():
    input("Presione enter para continuar...")
def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class NodoDoble:
    def __init__ (self , dato):
        """Clase del nodo con dos punteros para la lista doble enlazada"""
        self.dato = dato
        self.siguiente = None #Puntero al siguiente nodo
        self.anterior = None  #Puntero al nodo anterior
        

class ListaDobleEnlazada:
    def __init__ (self):
        self.cabeza = None
        self.cola = None
        self.actual = None #Puntero al nodo actual , para navegar por la lista doble enlazada
    
    def insertarDato(self , dato):
        """Inserta un nuevo nodo al final de la lista doble enlazada."""
        nuevoNodo = NodoDoble(dato)
        if self.cabeza is None: #Si la lista esta vacia o si la cabeza es None , el nuevo nodo sera la cabeza
            self.cabeza = self.cola = nuevoNodo #El nuevo nodo sera la cabeza y la cola
        else:
            self.cola.siguiente = nuevoNodo
            nuevoNodo.anterior = self.cola
            self.cola = nuevoNodo #El nuevo nodo sera la cola
    
    def mostrarSiguiente(self):
        """Muestra los nodos de la lista doble para adelante"""
        if self.actual is None:
            self.actual = self.cabeza

        if self.actual is not None:
            print(f"Nodo actual: {self.actual.dato}")
            if self.actual.siguiente is not None:
                self.actual = self.actual.siguiente
            else:
                print("Estas en el ultimo nodo , no podras continuar ;-; ")
        else:
            print("La lista esta vacia")
        #El fin de la lista doble enlazada es None
    def mostrarAnterior(self):
        """Muestra los nodos de la lista doble para atras"""
        if self.actual is None:
            self.actual = self.cola
        
        if self.actual is not None:
            print(f"Nodo actual: {self.actual.dato}")
            if self.actual.anterior is not None:
                self.actual = self.actual.anterior
            else:
                print("Estas en el primer nodo , no podras continuar ;-; ")
        else:
            print("La lista esta vacia")

#Nota mental , probablemente este metodo sea el mas costoso y largo , usare el metodo de la anterior lista como base para hacer este 
    def eliminarNodo(self ,dato):   #Este metodo tiene dos punteros para trabajar en la lista debido a su doble enlace
        """Elimina un nodo dependiendo del dato espesificado"""
        actual = self.cabeza #Se inicializa el nodo actual como la cabeza de la lista
        #Si la lista esta vacia , no se puede eliminar nada
        if not actual: 
            print("La lista esta vacia")
            return
        
        #Si el nodo/dato a eliminar es la cabeza , se cambia la cabeza al siguiente nodo
        if actual.dato == dato:
            self.cabeza = actual.siguiente #Si el nodo a eliminar es la cabeza , se cambia la cabeza al siguiente nodo
            if self.cabeza:
                self.cabeza.anterior = None #Se elimina la referencia al anterior nodo
            else:
                self.cola = None #Si la lista queda vacia , actualiza la cola
            del actual #El nodo actual se vuelve None para eliminarlo de la memoria
            print(f"El nodo {dato} fue eliminado del frente en la Base Nodera :D")
            return
        
        while actual and actual.dato != dato:  #Bucle while para recorrer la lista hasta encontrar el nodo a eliminar
            actual = actual.siguiente
        if not actual:
            print("El nodo no fue encontrado sorry :c")
            return
        
        #Si el nodo a eliminar es la cola 
        if actual == self.cola:
            self.cola = actual.anterior
            self.cola.siguiente = None #Se elimina la referencia al siguiente nodo
            del actual #El nodo actual se vuelve None para eliminarlo de la memoria
            print(f"El nodo {dato} fue eliminado de la cola en la base Nodera :0")
            return
        
        #Si el nodo a eliminar esta dentro del rango de la cabeza y la cola , se eliminara el nodo actual
        anterior = actual.anterior
        siguiente = actual.siguiente
        if anterior:
            anterior.siguiente = siguiente
        if siguiente:
            siguiente.anterior = anterior
        del actual
        print(f"El nodo {dato} fue eliminado de la Base nodera :D")
    
    def mostrarTodo(self):
        """Muestra todos los nodos de la lista doble enlazada"""
        actual = self.cabeza
        while actual:
            print(actual.dato , end=" ⇄ ")
            actual = actual.siguiente
        print("Ningun nodo mas por mostrar :D")

def main():
    baseNodera = ListaDobleEnlazada()
    while True:
        limpiarPantalla()
        print("1. Insertar nuevo nodo")
        print("2. Mostrar Todos los nodos")
        print("3. Eliminar Nodo")
        print("4. Navegar de nodo en nodo por la base Nodera")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            dato = input("Ingrese el dato del nuevo nodo: ")
            baseNodera.insertarDato(dato)
            print(f"Nodo {dato} insertado con exito!")
            pause()
        elif opcion == 2:
            print("Lista de nodos:")
            baseNodera.mostrarTodo()
            pause()
        elif opcion == 3:
            dato = input("Ingrese el dato del nodo a eliminar: ")
            baseNodera.eliminarNodo(dato)
            print(f"Nodo {dato} eliminado con exito!")
            pause()
        elif opcion == 4:
            print("Navegando en los nodos -.- ...:")
            while True:
                print("Hacia donde quieres ir?:")
                miniOpcion = int(input("1. Nodo Anterior \n2. Siguiente nodoc\n 3. Salir\n Seleccione una opcion: "))
                if miniOpcion == 1:
                    print("Navegando hacia el nodo Anterior")
                    baseNodera.mostrarAnterior()
                elif miniOpcion == 2:
                    print("Navegando hacia el nodo Siguiente")
                    baseNodera.mostrarSiguiente()
                elif miniOpcion == 3:
                    print("Saliendo...")
                    pause()
                    break
                else:
                    print("Opcion no valida")
                pause()
        elif opcion == 5:
            print("Saliendo...")
            pause()
            break
        else:
            print("Opcion no valida")
            break

if __name__ == "__main__":
    main()