#TALLER 3: PYTHON
#AUTHOR: Anderson Chila 
#FECHA :04 DEC 2023

from datetime import date
today = date.today()
print("Hoy es el dia", today)


a= int(input("digite el valor a:"))
b = int (input("digite el valor b:"))


if a>b:
    print("a es mayor que b")
else:
    print("a es menor que b")

print()
curso1= "requerimientos"
curso2= "algoritmos"

print("el curso uno es:", curso1)
print("el curso dos es:", curso2)

if curso1 == "requerimientos" and curso2 == "algoritmos":
    print("usted estudia programacion de software")
else:
    print("usted estudia algo diferente")
print()
print("finalizacion de la simulacion del sena")


frase= input("digite una oracion")
print("la frase en mayuscula es", frase.upper())
longitud= len(frase)
print("la longitud es de",  longitud , "caracteres")

if longitud > 10:
    print("tiene mas de 10 caracteres")
else:
    print("tiene menos de 10 caracteres")
print()
print("FIN")

