#TALLER 2 
#AUTHOR: Anderson Chila
#FECHA: 04 DEC 2023

from datetime import date
hoy = date.today()
print("Hoy es el dia" , hoy)
a=int(input("digite el primer numero"))
b=int(input("digite el segundo numero"))
c=int(input("digite el tercer numero"))

x= [a,b,c]
print("El valor maximo es:", max(x))
print("El valor maximo es:", min(x))
print("la suma de los tres valores es:", sum(x))
print()

z= float(input("digite un numero con decimales_: "))
redondo= round(z)
print ("el valor de ", z, "redondeado es:", redondo)
print()
frase= input("digite una oracion:")
print("La frase en mayuscula es:", frase.upper())
print("La frase en minuscula es:", frase.lower())

print("la frase con mayuscula inicial es: ", frase.capitalize())
print("la frase en mayuscula  es: ", frase.title())
print("la longitud de la cadena es: ", len(frase))
print()
print("fin")
