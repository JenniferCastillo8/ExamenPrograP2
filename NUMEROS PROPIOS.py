import random
numero = int(input("Ingrese un numero: "))
print("El numero ingresado es:", numero)

if numero == random.randrange(1,10):
    print("¡Adivinaste el numero!")
else:
    print("No adivinaste el numero :(")

print("El numero random era:", random.randrange(1,10))