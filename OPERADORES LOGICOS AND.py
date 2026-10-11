# ==========================================================
# Demostración de Operadores Lógicos en Python (and, or, not)
# ==========================================================


x = 5
y = 3
z = 5

print("--- 1. OPERADOR AND ---")
# Todas las condiciones deben ser True
resultado_and = (x > y) and (y > z)
print(f"({x} > {y}) and ({y} > {z}) -> {resultado_and}")  # True and False -> False
print()

print("--- 2. OPERADOR OR ---")
# Al menos una condición debe ser True
resultado_or = (x > y) or (y > z)
print(f"({x} > {y}) or ({y} > {z}) -> {resultado_or}")    # True or False -> True
print()

print("--- 3. OPERADOR NOT ---")
# Invierte el valor booleano
print(f"not True  -> {not True}")
print(f"not False -> {not False}")
print(f"not ({x} > {y}) -> {not (x > y)}")                   # not True -> False
print()

print("--- 4. EJEMPLO COMBINADO Y PRECEDENCIA ---")
# (x > y and x == z) or not (y > z)
parte_1 = (x > y and x == z)  # True and True -> True
parte_2 = not (y > z)         # not False -> True
resultado_combinado = parte_1 or parte_2

print(f"Expresión: (x > y and x == z) or not (y > z)")
print(f"Resultado final: {resultado_combinado}")