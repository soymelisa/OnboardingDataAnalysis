## Consultas Avanzadas

### OBJETIVO 
 - Fortalecer la capacidad de hacer preguntas perspicaces
 - Relacionar datos de diferentes tablas para ampliar nuestro espacio de preguntas

#### REQUISITOS 
1. MySQL Workbench
2. BD MySQL

#### DESARROLLO
Bienvenido al postwork de la sesión, este postwork es muy parecido al anterior. La idea es conseguir al menos dos tablas que se relacionan de alguna forma. Algunas veces vienen juntas en https://www.kaggle.com/datasets.  La dinámica es la misma que la anterior, pero ahora tenemos más datos y esto se pone más interesante. 

##### El script debe:
* Busca al menos dos datasets relacionadas que te parezcan interesantes y cárgalos sobre tu BD, te recomiendo buscar en https://www.kaggle.com/datasets

DATASET 01 - DB_RottenTomatoes
![liga](Sesion-04/DB_RottenTomatoes)
DATASET 02 - Oscars demographics
![liga](Sesion-04/Oscars-demographics-DFE.csv)

* Después de brevemente revisar los contenidos de tu BD, sin pensar en el SQL haz 5 preguntas que quizá podrías descubrir con los datos que tienes a la mano. Esta vez piensa de qué forma podrías extender tus preguntas tomando en cuenta la relación entre las tablas que tienes.

1) Qué tan frecuente es que los premiados en los Oscares se guían por el país para que incida en la decisión de ganar un premio
SELECT AVG(country * 
year_of_awardn) as MIN 
FROM movies

2) Qué tanto afecta la "streaming date"
SELECT * FROM resenas
WHERE StreamingDate BETWEEN #07/04/2015# AND #07/09/2020#;

3) Qué palabras son las más usadas en la columna 'Critic publication'  
4) Qué fuentes críticas tienen mayor relevancia en la decisión para otorgar un Oscar o subir de popularidad
GROUP BY 'Critic Publication'

5) Cómo se ve reflejado los demográficos de los Oscares en cuanto a religión y orientación sexual en cómo se evalúa el 'tatometer'
SELECT X.sexual_orientation, AVG(total) AS SXavg
FROM
(
SELECT A.genre, B.religion, year_of_award, SUM(quantityOrdered * year_of_award_gold) AS total
FROM _unit_id
GROUP BY year_of_award;


NOTA: Número de campo y dominio (campo) tienen que ser igual (?)


* Escribe la consulta para cada pregunta, si no tienes la suficiente información piensa en otra pregunta. 


SELECT *
FROM cast
WHERE (‘1980-01-01’ <= birth_date)
AND (birth_data <= ‘1989-12-31’)


Algo así como "producto cruz" si no lo hago bien (?)
SELECT *
FROM cast,audience_top_critics_count,rating C
AND C.rating > 5


