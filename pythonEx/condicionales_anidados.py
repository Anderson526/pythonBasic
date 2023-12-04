#TALLER 4
#AUTHOR: Anderson Chila
#FECHA: 04 DEC 2023

from datetime import date
today = date.today()
print("hoy es el dia" , today)
print()
print("EJERCICIO DE LAS CADENAS DE TRIANGULOS") 
a= int(input("digite el valor de a"))
b= int(input("digite el valor de b"))
c= int(input("digite el valor de c"))

if a==b and a==c and b==c:
    print("El triangulo es equilatero")
else:
    if a==b or b==c or a==c:
        print("El triangulo de isoseles")
    else:
        print("El triangulo es escaleno")
print()

animal = input("digite un animal")
animal = animal.upper()
if animal=="PERRO":
    print("Este animal es el mejor amigo del hombre:", animal)
elif animal =="GATO":
    print("este animal persigue a los ratones", animal)
elif animal == "OSO":
    print("Este animal vive en el polo norte", animal )
else:
    print("No es ninguno de los anteriores , este animal es:", animal)

print()
print("fin")

