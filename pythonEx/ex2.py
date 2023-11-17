#Autor: Anderson Chila
#Entrada de datos con input

#Todo se almacena mediante de variables
nombre = input("como es su nombre?")
#Se imprime en la variable la cual se almacena
print("su nombre es: "+ str(nombre))


#salida con caracteres especiales 

#\n salto de linea
print('soy un gato \nno soy un perro')

#\t tabulacion 

print('me gustan las manzanas \t pero no las peras')

#impresion de cadenas con funciones

frase1 = "hoy"
frase2 = " no "
frase3 = " tengo plata"


#basica
print(frase1 + frase2 + frase3)

#repeticion 
cadena = frase3 *3
print(cadena)

#capitalize
print(frase2.capitalize())
#lowercase
print(frase2.lower())
#uppercase
print(frase2.upper())

#manera recursiva para inicializar variables

a,b,c = 12,13,14
print(a+b+c)


#split nos ayuda para separar cadenas y almacenarlas en arrays o list

cadenatexto= "me .gusta. mucho el helado de .chicle"
arraycad= cadenatexto.split(".")
print(arraycad)

#repalce() cambia un dato especifico por otro

print(cadenatexto.replace("gusta", "odio"))