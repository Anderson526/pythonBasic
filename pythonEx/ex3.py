
#autor:Anderson Chila
#importacion de librerias

import datetime

fecha = datetime.datetime.now()
print("fecha hoy: " + str(fecha))

fechadia = datetime.date(2022,1,30)
print("fecha personalizada: " + str(fechadia) )


#resta de fechas

fechaaresta =   fechadia -fecha 

print(fechaaresta)