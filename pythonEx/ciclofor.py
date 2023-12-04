#TALLER PYTHON 5
#AUTHOR: Anderson Chila 
#FECHA: 04 dec 2023


from datetime import date
hoy = date.today()
print("Hoy es el dia:", hoy)
print()
print("TALLER 5 CICLOS ITERATIVOS CON SENTENCIA FOR")
num1= int(input("digite el numero a:"))
num2= int(input("digite el numero b(mayor):"))
print("ciclo para el primer numero")

for i in range(num1):
    print(i)
print("fin del ciclo")


print("iteracion de rangos de numero 1 a numero 2")

for i in range(num1,num2):
    print(i)
print("finalizacion de ciclo")

print()

print("iteracion de numero 1 hasta numero 2 con incremento de 2")

for i in range(num1, num2 , 2):
    print(i)

print("finalizacion de ciclo")

print()


print("iteracion por medio de caracteres")
empresa = input("ignrese el nombre de la empresa:")
empresa = empresa.lower()
for character in empresa:
    print(character)
print("finalizacion de ciclo")
print()



