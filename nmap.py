#Libreria para llamar al sistema operativo
import os
#Seleccionar segmento de red
red = "200.33.171.0/24"
#Rastrear red
os.system("nmap -sP " + red)