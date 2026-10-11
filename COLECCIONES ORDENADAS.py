#Colecciones Ordenadas

cancionesIronMaiden = ["Caught Somewhere in Time", "Killers", "Fear of the Dark", "Hallowed Be Thy Name", "Rime of the Ancient Mariner"]

print(" ")
print("El tamaño de la lista es: ", len(cancionesIronMaiden))

print(" ")
print(cancionesIronMaiden[0:3])

print(" ")
reverseList = cancionesIronMaiden[::-1]
print(reverseList)


for cancion in cancionesIronMaiden:
    print(cancion)