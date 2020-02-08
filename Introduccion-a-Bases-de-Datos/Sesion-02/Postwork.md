## Postwork

### OBJETIVOS
Aplicar los conceptos de la sesión a tu proyecto personal
Automatizar las tareas que sean factibles
Realizar consultas usando expresiones regulares
Realizar consultas haciendo uso de más de un archivo

### REQUISITOS
Git Bash instalado para equipos con Windows
Carpeta de repositorio actualizada

### DESARROLLO
En esta sesión ya debes de contar con un conjunto de datos definido y listo en una carpeta para trabajar.
Lo siguiente es que puedas formular consultas a tus datos, desde las consultas mas simples a las más complejas, a continuación se sugieren algunos casos.
Lo primero consiste en analizar el contenido de los archivos para determinar el formato en que se encuentran, si ya se encuentran en formato CVS, entonces no hay nada por hacer en este punto y puedes pasar a realizar consultas.
Hacer uso del comando head, tail, cat y sed para analizar, filtrar y reemplazar para transformar tus archivos a formato CSV (El formato JSON se verá más adelante).
Analizando el contenido de un archivo:
Datos $ head nombre-archivo.ext
[... primeras 10 líneas de tu archivo ...]

### Importante
No importa el tamaño de tus archivos, las herramientas de la terminal siempre serán tus amigas.
Reemplazando secciones de un archivo:
Datos $ sed "s/buscar/remplzar/g" nombre-archivo.dat | head
[... primeras 10 líneas del resultado ...]
Datos $


Guardando resultados en un archivo:

Datos $ sed "s/buscar/remplzar/g" nombre-archivo.dat > resultados.csv


Ya que los archivos están en formato CSV, entonces se puede iniciar a realizar consultas usando los comandos grep y wc
Datos $ grep -a CRITERIO archivo.csv | head
[... 10 primeras líneas del resultado ...]
Datos $


Si los resultados son satisfactorios entonces los contamos o guardamos, 
según sea el caso

Datos $ grep -a CRITERIO archivo.csv | wc
   n-lineas n-palabras n-bytes archivo.csv
Datos $


Se cuenta en número de líneas o registros
Datos $ grep -a CRITERIO archivo.csv > archivo-CRITERIO.csv
Datos $


Se guarda el resultado en un archivo.
Finalmente, si tus datos lo permiten, realiza consultas que involucren a más de un archivo o realizar consultas más complejas haciendo uso de expresiones regulares.
Recuerda que haciendo uso de herramientas desde terminal puedes hacer consultas con un mínimo de recursos y procesar grandes cantidades de información, por ejemplo, si quieres encontrar todos los registros que inicien con cierta palabra puedes usar:
Datos $ grep -aE ^Palabra archivo.csv | head

[... 10 primeras líneas de los resultados ...]

###  Nota:
Si tienes consultas que no puedas realizar es buen momento para comentarlo con tu Experta/o asignado para determinar si es factible realizar o hay que esperar a hacer uso de SQL.

### Doc:
https://docs.google.com/document/d/15LO4AkRNnmIQc2R5wyD-dp4YJKtNPVahyAsiR67q3jQ/edit?usp=sharing 