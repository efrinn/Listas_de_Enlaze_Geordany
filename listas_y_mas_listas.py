lista1 = []
lista2 = list()
                                    #Las variables son solo un apuntador a un espacio de memoria
lista1.append("George")
print(lista1)

lista1.append("John")
print(lista1)

lista1.insert(1, "Mary")
print(lista1)

lista1.insert(3, "Ana")
print(lista1)

lista1.insert(2, "Pedro")

lista2 = lista1.copy()
print(f"Lista 2: {lista2}")
print(f"Lista 1: {lista1}")

lista1.append("Otorrinolaringologo")

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

lista1.pop(0)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

del lista1[0]   #esta funcion elimina elementos por su posicion en la index
lista1.remove("Pedro") #esta funcion elimina elementos por su valor

lista1 = [name for name in lista1 if name != "Otorrinolaringologo"] #esta funcion elimina elementos por su valor
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")