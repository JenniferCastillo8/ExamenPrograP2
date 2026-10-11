palabra = "Python"
for letra in palabra:
    print(letra)

frutas = ["manzana", "naranja", "kiwi"]

# Uso de break (detiene todo el bucle)
for fruta in frutas:
    if fruta == "naranja":
        break
    print(fruta)

# Uso de continue (salta solo esa vuelta)
for fruta in frutas:
    if fruta == "naranja":
        continue
    print(fruta)

# Uso de else (corre al terminar de forma normal)
for fruta in frutas:
    print(fruta)
else:
    print("ya terminó el bucle")
    
    
    # Demostración funcional de las variantes de range() explicadas:
print("--- range(10) (0 a 9) ---")
for i in range(10):
    print(i)

print("--- range(3, 5) (3 y 4) ---")
for i in range(3, 5):
    print(i)

print("--- range(0, 10, 2) (Saltos de 2) ---")
for i in range(0, 10, 2):
    print(i)
    
frutas = ["manzana", "naranja", "kiwi"]
adjetivos = ["rica", "saludable"]

for adjetivo in adjetivos:
    for fruta in frutas:
        print(f"{fruta} {adjetivo}")
        
for i in range(10):
    pass        