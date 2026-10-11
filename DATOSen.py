ubicacion = ("Casa", "Trabajo")
ubicacion += ("Escuela",)  # Se crea una tupla nueva mediante concatenación
print(ubicacion)
categorias = {"Comida", "Bebida"}
categorias.add("Limpieza")
print(categorias)
precios = {"pan": 25}
precios["leche"] = 30
print(precios)
compras = ["pan", "leche"]
compras.append("huevos")
print(compras)
frutas = ["manzana", "naranja", "kiwi"]
for fruta in frutas:
    print(fruta)