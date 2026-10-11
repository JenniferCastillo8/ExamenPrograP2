# ==========================================================
# Demostración de Operadores de Asignación en Python
# ==========================================================

print("--- 1. SUMA Y RESTA CON ASIGNACIÓN ---")
x = 5
print(f"Valor inicial de x: {x}")
x += 3  # Equivale a x = x + 3
print(f"Después de x += 3: {x}")  # 8
x -= 3  # Equivale a x = x - 3
print(f"Después de x -= 3: {x}")  # 5
print()

print("--- 2. MULTIPLICACIÓN, DIVISIÓN Y OTROS ---")
x = 5
x *= 3
print(f"x *= 3 -> Resultado: {x} (Tipo: {type(x).__name__})")

x = 5
x /= 3
print(f"x /= 3 -> Resultado: {x} (Tipo: {type(x).__name__})")  # Siempre flotante

x = 5.0
x %= 2
print(f"x %= 2 -> Resultado: {x} (Tipo: {type(x).__name__})")

y = 20
y //= 2
print(f"y //= 2 (división entera) -> Resultado: {y}")

y = 10
y **= 3
print(f"y **= 3 (potencia) -> Resultado: {y}")
print()

print("--- 3. OPERADOR WALRUS (:=) ---")
# Asigna y devuelve el valor en la misma expresión
print(f"Valor asignado e impreso con Walrus (z := 3): {z := 3}")
print(f"Valor final de z: {z}")