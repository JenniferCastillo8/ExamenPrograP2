#Lo hizo: Sebastián GuadalupeTovar Negrete

nombre=input("Ingresa tu nombre: ")
calificaciones=[]
for i in range (3):
    calificacion=float(input(f"Ingrese la calificación {i + 1}:"))
    calificaciones.append(calificacion)

promedio=sum(calificaciones)/len(calificaciones)
print("Nombre: ",nombre)
print("Calificaciones: ", calificaciones)
print(f"Promedio: {promedio:.2f}")

if promedio>=6.0:
    print("Resultado: Aprobó")
else:
    print("Resultado: Reprobó")