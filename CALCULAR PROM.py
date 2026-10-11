#Lo hizo: Sebastián GuadalupeTovar Negrete

#Calcular el promedio
#Mostrar: nombre, calificaciones y promedio
# Indicar si aprobó (≥ 6.0) o reprobó


nombreEx=input("Ingresa el nombre de tu ex ")
calificacionesEx=[]
for i in range(3):
    calificacionEx=float(input(f"Ingrese la calificacion numero {i+1} de tu ex "))
    calificacionesEx.append(calificacionEx)

promedio=sum(calificacionesEx)/len(calificacionesEx)

if(promedio>=6.0):
    estado="Aprobado"
else:
    estado="Reprobado"

print("Tu ex de nombre: ",nombreEx)
print("Y de calificaciones: ",calificacionesEx)
print("Obtuvo un pormedio de: ",promedio)
print("Y por lo que el estado de tu ex es: ",estado)


