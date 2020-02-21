Postwork
## Fundamentos de MongoDB e importación de datos

### OBJETIVO
- [ ] Crear una Base de Datos en MongoDB para tú proyecto personal
- [ ] Crear las Colecciones necesarias para los distintos archivos
- [ ] Importar datos y validar la correcta importación
- [ ] Realizar consultas en base a filtrado de datos

### REQUISITOS
- [ ] Repositorio actualizado
- [x] Usar la carpeta de trabajo `Sesion-05/Postwork`
- [x] __MongoDB Compass__ iniciado y conectado al servidor de MongoDB
- [x] Carpeta de `Datos/` generado en el `Postwork` del la `Sesion-02`

### DESARROLLO

#### (1) Base de Datos

*Aquí pongan el nombre de su base de datos y la o las colecciones que crearon.*

```
Base de datos: MelisaPe_postwork
Colección: book_title
```

#### (2) Estructura del archivo CSV

*Aquí pongan el header del archivo CSV que usaron como dataset. La idea es que contrasten los documentos cargados en MongoDB con este header para asegurar que la carga fue correcta.*

{"_id":
    {"$oid":"5e4fde511e69422f6f837aca"}, 
    "bookID":"1",
    "title":"Harry Potter and the Half-Blood Prince (Harry Potter  #6)",
    "authors":"J.K. Rowling-Mary GrandPré",
    "average_rating":"4.56",
    "isbn":"0439785960",
    "isbn13":"9780439785969",
    "language_code":"eng",
    "# num_pages":"652",
    "ratings_count":"1944099",
    "text_reviews_count":"26249"}

```
bookID,title,authors,avarage_rating,isbn,isbn13,language_code,# num_pages, ratings_count,text_reviews_count
```

#### (3) Consultas

*Aquí pongan las consultas que pensaron y como primera línea pongan con qué la van a ejecutar, es decir, un filtro, proyección, ordenamiento, etc.*

1. Realizar consultas a tus datos por medio de realizar filtrado de datos, respondiendo a preguntas como:
   - ¿cuántos registros hay de cierto tipo o categoría?
   - ¿cuántos registros hay de dos o más categorías?
   - ¿cuántos registros hay donde un campo sea mayor, meno o igual a cierto valor?
   - ¿cuántos registros tienen un campo que puede o no pertenecer a una lista de valores?
   - O preguntas que utilicen alguna combinación de las anteriores

   __Meta 2:__ Lograr responder a preguntas con resultados útiles.


1. ¿Pregunta 1?

*Solución:*

```json
// FILTER
{campo: "Valor"}
```

2. ¿Pregunta 2?

*Solución:*

```json
// SORT
{campo: -1}
```

3. ¿Pregunta 3?

*Solución:*

```json
// PROJECTION
{campo: 1}
```
