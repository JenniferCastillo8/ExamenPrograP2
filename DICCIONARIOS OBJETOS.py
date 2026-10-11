
# 1. Creación del diccionario inicial
alumno = {
    "nombre": "Ana López",
    "grupo": "3A",
    "calificaciones": [8.5, 9.0, 7.5]
}

print("--- Acceso a un valor ---")
print(alumno["nombre"])  # Imprime: "Ana López"

print("\n--- Agregar y modificar elementos ---")
alumno["email"] = "ana@mail.com"  # Agrega una nueva clave-valor
alumno["grupo"] = "3B"            # Modifica el valor existente de "grupo"
print("Diccionario actualizado:", alumno)

print("\n--- Recorrer clave y valor (.items()) ---")
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

print("\n--- Recorrer solo valores (.values()) ---")
for valor in alumno.values():
    print(valor)

print("\n--- Recorrer solo claves ---")
for clave in alumno:
    print(clave)