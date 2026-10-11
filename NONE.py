
print("=== 1. ¿QUÉ ES NONE? ===")
x = None
print("Valor de x:", x)                    # None
print("Tipo de x:", type(x))              # <class 'NoneType'>
print()

print("=== 2. NO ES LO MISMO QUE 'VACÍO' ===")
valores = ["", 0, False, [], None]
for v in valores:
    print(f"Valor: {repr(v):<8} | Tipo: {type(v)}")
print()

print("=== 3. NONE NO ES IGUAL A FALSE O A 0 ===")
print("type(False):", type(False))  # <class 'bool'>
print("type(0):     ", type(0))      # <class 'int'>
print("type(None):  ", type(None))  # <class 'NoneType'>
print()

print("=== 4. FUNCIONES QUE NO DEVUELVEN NADA ===")
def saludar():
    print("Hola")
    # No hay return explícito

resultado = saludar()
print("Resultado de la función:", resultado)         # None
print("Tipo del resultado:     ", type(resultado))  # <class 'NoneType'>
print()

print("=== 5. ¿CÓMO IDENTIFICAR NONE? ===")

if x is None:
    print("x no tiene valor (es None)")
else:
    print("x tiene un valor asignado")