https://github.com/Any7200/itesm-tc1033-a01366974.git

Para ejecutar el programa, se necesita incluir en la carpeta en la que se encuentra el código fuente el archivo "datos_vuelos.csv", después de eso sólo se necesita ejecutar el código y comprobar los cambios en el archivo "resultados.csv"

Diagrama

- No utilice herencia en ningun momento, me parecía que no era completamente necesario y que quedaba mejor con asociasiones
- Las asosiación de agregación que utilice la puse ya que el vuelo puede utilizar métodos y tener atributos sin la necesidad de pasajeros
- Puse algunos métodos extra, para que el diagrama tuviera más lógica
- Utilice una asosiación de composición de la clase reporte a la clase vuelo, ya que puede haber vuelos sin reporte, pero no reporte sin vuelos