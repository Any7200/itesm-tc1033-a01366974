# Proyecto final POO
    En esta carpeta se encuentra la fusión de la solución de la tarea 3, realizada por el profesor, la cual generaba reportes, junto con el proyecto de la clase, el cual despliega un menu para agregar o modificar los datos del sistema de un supuesto aeropuerto
        1.Se agregaron los métodos en la clase AirportAD, ya que manipula indormación y la almacena
        2.En el apartado del cógigo que corresponde al reporte estadístico, faltaban generar para los pasajeros y para los vuelos "landed" y "departured"; como en el estatus no había dato alguno que se relacionara totalmente con este último (departured), tomamos en su lugar la variable "in transit", puesto que era el que más se asemejaba a departures.
        3.A pesar de todos los intentos hechos, el programa no logra reescribir los archivos ni generar el reporte, ya que al crear otro objeto de la clase "Airport", los atributos vuelven a quedar en None y no permiten trabajar con los diccionarios que se guardan en memoria
        4.Tanto agregar como modificar funcionan perfectamente, todos los datos son guardados en memoria
        5.El programa está prácticamente listo, lo único que faltaría resolver sería el conflicto con los atributos de tipo None
        6.De todas formas, todos los métodos y clases están hechos para que, si el conflicto se resolviera, pudiera funcionar debidamente
        7.Se busco durante muchas horas como solucionarlo