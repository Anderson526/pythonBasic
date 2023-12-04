#Taleer 1 python 
#author : Anderson Chila
#Fecha: 04 diciembre 2023

from datetime import date
today= date.today()
print("Hoy es el dia: ", today)

n1= int(input("digite el primer numero "))
n2= int(input("digite el segundo numero"))

suma = n1+n2
resta = n1-n2
producto = n1*n2
division = n1/n2

print("la suma es = ", suma)
print("la resta es = ", resta)
print("la multiplicacion es = " , producto)
print("la division es ", division)

print("fin")