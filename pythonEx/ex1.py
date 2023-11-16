#Autor: Anderson Chila 
#tipos de datos en numeros


decimal= 8
binario=0b1101
octal=0o11
hexadecimal=0xc


#output de una variable

print(f"numero en decimal:{decimal}")
print("numero en binario:"+str(binario))
print(f"numero en octal: {octal}")
print("nuemro en hexadecimal:"+str(hexadecimal))



#numeros flotantes 
#estos pueden tener una cantidad aproximada el problema es que tienden a ser mas de 10 digitos

real1= 1.1+2.2
print("resultado de la suma decimal es: " + str(real1))

#se puede condensar o simplificar con la funcion round(var,n-decimales)

print("resultado de la suma decimal es:" + str(round(real1,1)))


#lista de items (list) estas son considerados como arreglos de toda la vida

newLista = [3,2,'miau',[2,3,4],6]


print ("llamado al valor del areglo [3][2]:" + str(newLista[3][2]))

#Lista en tuplas es muy similar a los arreglos o listas 
#tuples in list, is very similar to arrays or lists in js

newtupla = ("var1",2,3)

print("longitud de la tupla: "+str(len(newtupla))) # saca el numero de elementos de la tupla
#get the number of elements to tuple




#sets 
#unorded collection of elements which are not repited 

newgroup = set([1,2,3,4,5,6,7,8,"maiu"])
print("nuevo grupo:"+str(newgroup))





#examples about dictionaries , this method is called like map

futbolistas = dict()


futbolistas = {

13 : "Mina", 21 : "Lucumi",

17 : "Fabra", 11 : "Cuadrado",

9 : "Falcao", 19 : "Muriel",

15 : "Uribe", 10 : "James Rodriguez",

16 :"Lerma", 5 : "Wilmar Barrios",

3 : "Murillo"

}


print("diccionario de futbolistas:")
print(futbolistas)
print (futbolistas[16])




#type and isinstance 
#type identify what type is the element selected 

print(type(futbolistas))

#isinstance helped to recognize if a specific type merge with the data 

print(isinstance(futbolistas,bool)) #is false cuz i managed a dictionary or dict

##type of data conversion 

#str() string characters
#int() natural entire number
#float() double or decimal number


ingresos = "29384872"

ingresos  = int(ingresos) + 10

print(ingresos)

ingresos = str(ingresos)
print("ingresos de:" + ingresos)





