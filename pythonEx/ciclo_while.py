#TALLER 6 PYTHON 
#AUTHOR: Anderson Chila
#FECHA: 04 dec 2023

from datetime import date
hoy = date.today()

print("hoy es el dia:", hoy)
print()
print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
num1= int(input("digite un numero:"))

print("ciclo controlado por medio de un contador:")
i=1

while i<= num1:
    print(i)
    i +=1
print("fin del ciclo")
print()


print("ciclo controlado por un evento")

i=1
numero1=5
nuemro2= int(input("ingrese un numero del 1 al 10:"))
while nuemro2 != numero1:
    i+=1
    nuemro2= int(input("digite un numero del 1 al 10"))
print("acertaste en el intento n", i)
print("fin del cliclo")

print(  "ciclo abordado con la sentencia break")
amistad= input("digite nombre de una amistad:")
amistad= amistad.upper()
for characte  in amistad:
    print(characte)
    if characte =="A":
        break 
print("fin del ciclo")
print()
print("fin")