#Lo hizo: Sebastián GuadalupeTovar Negrete
edad=18;
tiene_identificacion=True;
es_estudiante=False

if (edad>=18 and tiene_identificacion):
    print("Cumple ambas condiciones");
if (edad>=18 or es_estudiante):
    print("Cumple al menos una condicion");

if not es_estudiante:
    print("No es estudiante")