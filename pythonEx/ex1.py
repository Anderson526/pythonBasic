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


newtupla = ("var1",2,3)

print("longitud de la tupla: "+str(len(newtupla))) # saca el numero de elementos de la tupla




#conjuntos 
#coleccion no ordenada de elementos los cuales no se repiten 

newgroup = set([1,2,3,4,5,6,7,8,"maiu"])
print("nuevo grupo:"+str(newgroup))
