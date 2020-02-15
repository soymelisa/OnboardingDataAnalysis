(../../Readme.md) > [`Sesión 03`](../Readme.md) > Postwork
## Postwork

### OBJETIVOS
- Crear u obtener una base de datos SQL para tú proyecto personal
- Crear las tablas necesarias para los distintos archivos
- Importar datos y validar la correcta importación
- Contar con tú conjunto de datos importado en un Servidor MariaDB/MySQL

### REQUISITOS
1. __Git Bash__ instalado para equipos con Windows
1. __Mycli__ instalado
1. Datos de conexión al Servidor MariaDB o MySQL y con permisos para ejecutar la instrucción `LOAD DATA LOCAL INFILE`.
1. Carpeta de `Datos/` generado en el `Postwork` del la `Sesion-02`
1. Carpeta de repositorio actualizada

### DESARROLLO
En esta sesión se hará uso de la carpeta de Datos que se generó en la `Sesion-02`, se espera que tengas uno o más archivos en formato CSV

1. Haz que tu carpeta de trabajo sea `Introduccion-a-Bases-de-Datos/Sesion-03/Postwork/`
   ```console
   $ cd Introduccion-a-Bases-de-Datos/Sesion-03/Postwork
   Postwork $
   ```

1. Copiar la carpeta `Datos` creada en el `Sesion-02/Postwork/` y moverse a la carpeta `Datos/`
   ```console
   Postwork $ cp -a ../../Sesion-02/Postwork/Datos .
   Postwork $ cd Datos
   Datos $
   ```

1. Para cada archivo CSV realizar el proceso:
   - Analizar contenido del archivo
![imagenpostwork1](screenshots/01_Analizar-contenido-del-archivo.png)

   - Definir lista de campos y tipos de datos para cada uno
`Users` en SQL: 
   - __id__ INT PRIMARY KEY
   - __genero__ VARCHAR(1)
   - __edad__ INT
   - __ocup__ INT
   - __cp__ VARCHAR(20)

![imagenpostwork1](screenshots/users_part-01.png)

`Movies` en SQL: 
   - __MovieID__ INT PRIMARY KEY
   - __Title__ VARCHAR(1)
   - __Genres__ VARCHAR(20)
   
![imagenpostwork1](screenshots/movies_03-01.png)

`Ratings` en SQL: 
   - __UserID__ INT PRIMARY KEY
   - __MovieID__ INT SECONDARY KEY
   - __Rating__ INT
   - __Timestamp__ VARCHAR(20)

![imagenpostwork1](screenshots/Ratings_info.png)

   - Realizar conexión al Servidor MariaDB/MySQL usando el comando `mycli`

![imagenpostwork1](screenshots/1_Conectarme_.png)

   - Hacer uso de tu base de datos con la instrucción SQL `USE`
![imagenpostwork1](screenshots/use_4DB.png)

   - Crear la tabla usando la instrucción `CREATE` en SQL
![imagenpostwork1](screenshots/Create_DB.png)

   - Importar datos a la tabla usando la instrucción `LOAD` y habilitando los permisos para `mycli` con la opción `--local-infile true`
![imagenpostwork1](screenshots/--local-infile--true.png)
![imagenpostwork1](screenshots/Load_Data_Local_Infile.png)
![imagenpostwork1](screenshots/SelectAllFromUsersLimit10.png)
![imagenpostwork1](screenshots/Truncate_users.png)

   - Validar que los datos se hayan importado correctamente haciendo uso de la instrucción `SELECT` tanto a nivel de campos, como en el número de registros importados.
MelisaPerez> LOAD DATA LOCAL INFILE "users.csv" INTO TABLE users FIELDS TERMINATED BY ",";
![imagenpostwork1](screenshots/Select_correct_2.png)
![imagenpostwork1](screenshots/COUNT_Users.png)


__Meta:__ Toma en cuenta que tu objetivo es que logres contar con todo tu conjunto de datos importado en el servidor para más adelante poder realizar consultas.

__Sugerencia:__ Si tienes problemas al realizar algunos de los pasos del procedimiento es buen momento para comentarlo con tu __Experta/o__ asignado para determinar la mejor solución.


