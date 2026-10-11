# --- CÓDIGO COMPLETO: COLECCIONES EN PYTHON ---

print("--- 1. TUPLA (Ordenada e inmutable) ---")
t = (10, "hola", 3.5)
print("Acceso por índice [1]:", t[1])  # Imprime: hola

print("\n--- 2. LISTA (Ordenada y mutable) ---")
l = [1, 2, 3]
l.append(4)
print("Lista modificada:", l)  # Imprime: [1, 2, 3, 4]

print("\n--- 3. DICCIONARIO (Pares clave-valor) ---")
d = {"nombre": "Ana", "edad": 25}
print("Acceso por clave 'nombre':", d["nombre"])  # Imprime: Ana

print("\n--- 4. CONJUNTO / SET (No ordenada, elementos únicos) ---")
s = {1, 2, 2, 3}
print("Conjunto limpio de duplicados:", s)  # Imprime: {1, 2, 3}

print("\n--- 5. COLECCIÓN (Término genérico - Ejemplo complementario) ---")
def procesar_generica(coleccion):
    print(f"Estructura [{type(coleccion).__name__}]: {coleccion}")

procesar_generica((1, 2))             # Tupla
procesar_generica([3, 4])             # Lista
procesar_generica({"a": 1})           # Diccionario
procesar_generica({5, 6})             # Conjunto