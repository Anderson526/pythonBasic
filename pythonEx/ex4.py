x= 10
if x > 29:
    print(str(x) +" es mayor")
else:
    print(str(x) + " es menor")


    temperatura = 25
lluvia = False

if temperatura > 20 and not lluvia:
    print("Es un buen día para salir.")
elif temperatura <= 20 or lluvia:
    print("Mejor quédate en casa.")






puntuacion = 50
tiempo = 48
vidas = 2

if tiempo < 50:
    print("tu tiempo se esta agotando")
    if puntuacion > 50 and vidas == 2:
        print("puntuacion perfecta")
    else:
        print("su puntuacion ha sido mala")
else:
    print("todavia tienes tiempo") 
 

#este tipo de funciones se utilizan en ciclos o bucles como pueden ser el ciclo for 
#for i in range(10, 0, -2):
#range(valor_inicial, valor_final, incremento/decremento)



ensalada = {'Manzana':'verde', 'Patilla':'rosado', 'Banano':'amarillo', 'Papaya':'naranja'}
#ciclo por medio de una lista
for elemento,elemento2 in ensalada.items():
    print (str(elemento)+ str(elemento2))


for i in range(1,5,1):
    print(i, i*21)







intentos = 1
valmax = 100

valdigitado = int(input("ingrese un numero del 1 al 100:"))

while valdigitado != valmax:

    valdigitado = int(input("ingrese un numero del 1 al 100:"))
    intentos +=1

print("acertaste en ", intentos)


