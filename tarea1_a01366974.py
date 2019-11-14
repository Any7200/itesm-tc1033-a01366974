#A01366974 ANA LAURA RODRIGUEZ JURADO
import csv
archivo=open("datos_vuelos.csv","r")
texto=csv.reader(archivo)
lista_1=list(texto)
sorted_1=sorted(lista_1, key=lambda salida: salida[1])
archivo=open("resultados.csv","w+")
archivo.write("Mes, Pais, % de vuelos")
archivo.write("\n")
for line in sorted_1:
    archivo.write(",")
    archivo.write("\n")
archivo.close()
