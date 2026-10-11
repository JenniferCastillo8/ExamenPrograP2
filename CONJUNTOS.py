#CONNJUNTOS
frutas = {"manzana", "naranja", "mandarina", "naranja"}
print(frutas) #{"manzana", "naranja", "mandarina"}
print(type(frutas)) #<class 'set'>
print(len(frutas)) #El duplicado lo ignora
#VERIFICAR ELEMENTOS
print("manzana" in frutas) #True
print("pera" not in frutas) #True
#AGREGAR ELEMENTOS
frutas.add("pera")
print(frutas)
#ELIMINAR ELEMENTOS
#remove(x)
s = {1, 2, 3}
s.remove(2)
print(s)
#discard(x)
s.discard(5)
print(s)
#pop
s.pop() #aleatorio
print(s) #cambia cada vez
#clear
s.clear()
print(s) #set()

#PROGRAMA PROPIO CONJUNTOS
conjunto = {"Python", "Java", "C", "Python"}
print(conjunto)
print(len(conjunto))
print("Java" in conjunto)
conjunto.add("Go")
print(conjunto)