texto = "Este es un texto"

print(texto[0])
print(texto[4])

#slicing: no incluido
texto = "Este es un texto"
print(texto[0:4])
print(texto[:7])
print(texto[5:])
print(texto[5:-2])

#remplazar replace()
curso = "esto es un curso de python"
print(curso.replace("python", "java"))

#dividir: split()

texto = "Esto es un texto"
texto_dividido = texto.split(" ")
print(texto_dividido)

#comparar sin errores

texto2 = "Esto es un texto tiene MAYUSCULAS y minusculas"
busqueda = "mayusculas"

print(busqueda in texto2)
print(busqueda.lower() in texto2.lower())