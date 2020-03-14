`Data Science` > [`Programacion con R`]
## Exploracion de datos

### OBJETIVO
- Aprender a extraer información de un dataframe.  

#### REQUISITOS
1. Contar con R studio.
1. Usar la carpeta de trabajo `Sesion04/Ejemplo-03`

#### DESARROLLO

Instalamos el paquete de datos de Titanic.

install.packages('titanic')

library(dplyr)
library(titanic)
names(titanic_train)

str(titanic_train)
head(titanic_train)
nrow(titanic_train)
ncol(titanic_train)

# Transformamos en factor
titanic_train$Survived <- factor(titanic_train$Survived)

Supervivencia: ¿Cuál fue el número de sobrevivientes?
```{r}
sobrev <- titanic_train %>%
  group_by(Survived) %>%
  count()

print(sobrev)
```

![imagenretos_s04](Screenshots_S04/S04_Ejemplo3.JPG)


Clase: ¿Cuál fue la cantidad de pasajeros en cada clase?
```{r}
clases <- titanic_train %>%
  group_by(titanic_train$Pclass) %>%
  count()

print(clases)
```

Sexo: ¿Cuántos hombres y mujeres a bordo?

```{r}
sex <- titanic_train %>% 
  group_by(titanic_train$Sex) %>% 
  count()

print(sex)
```

![imagenretos_s04](Screenshots_S04/S04_Ejemplo3_group_by__titanic.JPG)


Edad: ¿Cuál era el promedio de edades de los pasajeros?

```{r}
mean(titanic_train$Age, na.rm = TRUE) #el segundo argumento en funcion mean elimina valores nulos del dataframe.

```


