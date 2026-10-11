# Operaciones con listas

valores = [10, 20, 30, 40, 50]

print(max(valores))
print(min(valores))
print(sum(valores))

promedio = sum(valores) / len(valores)
print(promedio)

Primeros3Val = valores[:3]
print(Primeros3Val)

filtrada = [x for x in valores if x > 25]
print(filtrada)