alumno = {
    "nombre": "Ana López",
    "grupo": "3A",
    "calificaciones": [8.5, 9.0, 7.5]

}
#Acceder
print(alumno["nombre"]) #"Ana López"

#Agregar / modificar
alumno["email"] = "ana@mail.com"
alumno["grupo"] = "3B"

#Recorrer
#CLAVE Y VALOR
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

#Valores
for valor in alumno.values():
    print(valor)
#Claves
for clave in alumno:
    print(clave)

#PROGRAMA PROPIO DICCIONARIOS
diccionario = {
    "nombre": "Miguel",
    "carrera": "Mecatrónica",
    "semestre": 1
}
print(diccionario)
print(diccionario["nombre"])
diccionario["semestre"] = 1
diccionario["escuela"] = "ITC"
for clave, valor in diccionario.items():
    print(clave, ":", valor)