# ComparaCervezasSupermercado
Realizar comparación de precios a partir de una marca de cerveza en dos supermercados conocidos en Chile, los cuales son Lider.cl y Tottus.cl

Primero, se realiza web scraping a los sitios lider.cl y tottus.cl, solo especificando el tipo de producto "cerveza". Lo anterior, nos devuelve los datos que necesitamos y los exportamos a archivos .json (es solo para un ambiente educativo).

Luego de tener un archivo .json para los datos de cada supermercado, ejecutamos nuestro script, indicando que marca de cerveza queremos y nos devolverá todos los items asociados a esa marca y su respectivo valor.

Cabe mencionar que no está filtrado totalmente, por lo que se agrega la columna descripción para poder entender bien si el producto es un pack, una lata, una botella, etc.
