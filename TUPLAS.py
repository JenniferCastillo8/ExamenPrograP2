#TUPLAS
#CONCEPTO CLAVE
tecnologias = ("Python", "JavaScript", "Go")
print(tecnologias)
print(type(tecnologias))
print(tecnologias[1])
#TUPLA DE UN SOLO ELEMENTO
fruta = ("manzana",) #SI NO TIENE COMA, NO ES TUPLA
print(type(fruta))
#MIX DE TIPOS Y DESEMPAQUETADOS
tupla = ("Python", 5, True)
print(type(tupla))
x, y, z = tupla
print(x)
print(y)
print(z)
#CONCATENAR Y DUPLICAR
tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)
tupla3 = tupla1 + tupla2
print(tupla3)
tupla = ("A", "B", "C")
print(tupla * 2)
#RECORRER CON FOR
colores = ("Rojo", "Verde", "Azul")
for color in colores:
    print(color)
#MODIFICAR UNA TUPLA
tupla_a_modificar = ("Python", "JavaScript", "Go")
lista_comodin = list(tupla_a_modificar)
lista_comodin.append("ReactJS")
tupla_a_modificar = tuple(lista_comodin)
print(tupla_a_modificar)

#PROGRAMA PROPIO TUPLA
mi_tupla = (1, 2, 3)
print(mi_tupla)
print(mi_tupla[0])
print(len(mi_tupla))