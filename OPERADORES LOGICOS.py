# ==========================================================
# Demostración de Operadores Aritméticos en Python
# ==========================================================

# 1. Definición de variables base
x = 5
y = 10

print("--- 1. SUMA Y RESTA ---")
print(f"x + y = {x + y}")  # 15
print(f"x - y = {x - y}")  # -5
print()

print("--- 2. MULTIPLICACIÓN Y DIVISIÓN ---")
print(f"x * y = {x * y}")          # 50
print(f"y / x = {y / x}")          # 2.0 (La división normal siempre da float)
print()

print("--- 3. MÓDULO, POTENCIA Y DIVISIÓN ENTERA ---")
# Módulo % (residuo de la división)
print(f"12 % 5 = {12 % 5}")        # 2
# Potencia ** (eleva a la potencia)
print(f"y ** x = {y ** x}")        # 100000 (10 elevado a la 5)
# División entera // (quita decimales)
print(f"12 // 5 = {12 // 5}")      # 2
print()

print("--- 4. APLICACIÓN PRÁCTICA: DETECTAR NÚMEROS PARES ---")
par = 8
es_par = (par % 2 == 0)
print(f"¿El número {par} es par? {es_par}")  # True
print()

print("--- 5. ORDEN DE PRECEDENCIA Y USO DE PARÉNTESIS ---")
# Jerarquía: 1. Paréntesis, 2. Exponentes (**), 3. Multiplicación/División (*, /, //, %), 4. Suma/Resta (+, -)
resultado_sin_parentesis = 10 + 5 * 2
resultado_con_parentesis = (10 + 5) * 2

print(f"10 + 5 * 2 = {resultado_sin_parentesis}")         # 20 (Multiplica primero)
print(f"(10 + 5) * 2 = {resultado_con_parentesis}")       # 30 (Suma primero gracias al paréntesis)