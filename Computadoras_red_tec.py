#Libreria para llamar al sistema operativo
import os
#Definimos los octetos de la red

hostname = "200.33.171."
i=0
cont=0
while i<256:
    respuesta = os.system("ping " + hostname + str(i))
    if respuesta==0:
        cont+=1
    i+=1
print (" El número de host activos es: "+ str(cont))

