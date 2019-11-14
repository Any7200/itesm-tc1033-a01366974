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
print(lista_1)
archivo=open("resultados.csv","r")
lectura=csv.reader(archivo)
lista_2=list(lectura)
print(lista_2)
for x in range(0,32):
    if sorted_1[x][1].find(" 1801")!=-1:
        lista_2[x+1][0]="Enero"
    elif sorted_1[x][1].find(" 1802")!=-1:
        lista_2[x+1][0]="Febrero"
    elif sorted_1[x][1].find(" 1803")!=-1:
        lista_2[x+1][0]="Marzo"
    elif sorted_1[x][1].find(" 1804")!=-1:
        lista_2[x+1][0]="Abril"
    elif sorted_1[x][1].find(" 1805")!=-1:
        lista_2[x+1][0]="Mayo"
    elif sorted_1[x][1].find(" 1806")!=-1:
        lista_2[x+1][0]="Junio"
    elif sorted_1[x][1].find(" 1807")!=-1:
        lista_2[x+1][0]="Julio"
    elif sorted_1[x][1].find(" 1808")!=-1:
        lista_2[x+1][0]="Agosto"
    elif sorted_1[x][1].find(" 1809")!=-1:
        lista_2[x+1][0]="Septiembre"
    elif sorted_1[x][1].find(" 1810")!=-1:
        lista_2[x+1][0]="Octubre"
    elif sorted_1[x][1].find(" 1811")!=-1:
        lista_2[x+1][0]="Noviembre"
    elif sorted_1[x][1].find(" 1812")!=-1:
        lista_2[x+1][0]="Diciembre"
    else:
        lista_2[x+1][0]="-"
for y in range(0,32):
    if sorted_1[y][0].find("D")!=-1:
        lista_2[y+1][1]="Alemania"
    elif sorted_1[y][0].find("PP")!=-1:
        lista_2[y+1][1]="Brasil"
    elif sorted_1[y][0].find("CF")!=-1:
        lista_2[y+1][1]="Canada"
    elif sorted_1[y][0].find("A7")!=-1:
        lista_2[y+1][1]="Catar"
    elif sorted_1[y][0].find("CC")!=-1:
        lista_2[y+1][1]="Chile"
    elif sorted_1[y][0].find("B")!=-1:
        lista_2[y+1][1]="China"
    elif sorted_1[y][0].find("OY")!=-1:
        lista_2[y+1][1]="Dinamarca"
    elif sorted_1[y][0].find("HC")!=-1:
        lista_2[y+1][1]="Ecuador"
    elif sorted_1[y][0].find("A6")!=-1:
        lista_2[y+1][1]="Emiratos Arabes"
    elif sorted_1[y][0].find("EC")!=-1:
        lista_2[y+1][1]="Espana"
    elif sorted_1[y][0].find("N")!=-1:
        lista_2[y+1][1]="Estados Unidos"
    elif sorted_1[y][0].find("PK")!=-1:
        lista_2[y+1][1]="Indonesia"
    elif sorted_1[y][0].find("JA")!=-1:
        lista_2[y+1][1]="Japon"
    elif sorted_1[y][0].find("XA")!=-1:
        lista_2[y+1][1]="Mexico"
    elif sorted_1[y][0].find("9V")!=-1:
        lista_2[y+1][1]="Singapur"
    elif sorted_1[y][0].find("HS")!=-1:
        lista_2[y+1][1]="Tailandia"
    else:
        lista_2[y+1][1]="-"
lista_2.remove(lista_2[0])
lista_2.remove(lista_2[-1])
print(lista_2)
dicc={}
valor=-1
for lines in lista_2:
    valor+=1
    mes=lista_2[valor][0]
    pais=lista_2[valor][1]
    if mes not in dicc.keys():
        dicc[mes]={}
    elif pais not in dicc[mes].keys():
        dicc[mes][pais]=1
    else:
        dicc[mes][pais]+=1
total_por_mes={}
for mes in dicc:
    total_mes=0
    for pais in dicc[mes]:
        total_mes+= dicc[mes][pais]
        total_por_mes[mes]=total_mes
lista_3=[]
porcentaje={}
for mes in dicc:
    for pais in dicc[mes]:
        total_mes_pais=(dicc[mes][pais]/total_por_mes[mes])*100
        if mes not in porcentaje.keys():
            porcentaje[mes]={}
        porcentaje[mes][pais]=round(total_mes_pais, 2)
        if dicc[mes] not in lista_3:
            lista_3.append([mes,pais,porcentaje[mes][pais]])
archivo.close()
valor=-1
for rows in lista_3:
    valor+=1
    if lista_3[valor][2]<20:
        lista_3.remove(lista_3[valor])
        valor-=1
print(lista_3)
archivo=open("resultados.csv","w+")
archivo.write("Mes, Pais, % de vuelos")
archivo.write("\n")
writer=csv.writer(archivo)
writer.writerows(lista_3)
archivo.close()
#PROFE, JOSE ME ESTUVO AYUDANDO UN POCO CON PEQUEÑAS PARTES DEL CODIGO
#ME COMENTO QUE USTED LO ASESORO EN EL DESARROLLO DE LA TAREA
#ME COMPARTIO ALGUNAS FUNCIONES Y METODOS, TALES COMO "SORTED" Y FUNCIONES CON CSV
