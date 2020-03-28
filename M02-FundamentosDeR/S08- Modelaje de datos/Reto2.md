
## Inicio al modelaje de datos

### OBJETIVO
- Crear un algoritmo knn

#### REQUISITOS
1. Contar con R studio.
1. Usar la carpeta de trabajo `Sesion08/Reto-02`

#### DESARROLLO
Para nuestro modelo de clasificacion knn seguiremos los siguientes pasos: 
* Usaremos el dataset llamado "diamonds" ya disponible en R con el package ggplot2. 
´´
library(ggplot2)
´´

* Lo guardaremos como data frame como "diamantes"
´´
diamantes <- data.frame(diamonds)
´´

* Crearemos un numero aleatorio con el 90% de las filas (llamado random)
´´
random <- sample(1:nrow(diamantes),0.9 * nrow(diamantes))
´´

* Crearemos una funcion de normalizacion (llamada normalizado)
´´
normalizado <-function(x) { (x -min(x))/(max(x)-min(x))}
´´

* Normalizaremos los datos y los guardaremos como diamantes_normalizado
´´
diamantes_normalizado <- as.data.frame(lapply(diamantes[,c(1,5,6,7,8,9,10)], normalizado))
´´

* Extraemos el training set y test set
´´
diamantes_trainining <- diamantes_normalizado[random,]
diamantes_test <- diamantes_normalizado[-random,] 
´´

* Extraemos la segunda columna (variable) y la guardamos como factor, ya que es una variable categorica en lugar de numerica (como diamantes_categoria_target). Haremos la misma conversion para test (diamantes_categoria_test)
´´
diamantes_categoria_target <- as.factor(diamantes[random,2])
diamantes_categoria_test <- as.factor(diamantes[-random,2])
library(class)
´´

* Correremos la funcion de prediccion con knn (gracias al package class)
´´
predic <- knn(diamantes_trainining,diamantes_test,cl=diamantes_categoria_target,k=20)
´´

* Creamos la confusion matrix
´´
con_mat <- table(predic,diamantes_categoria_test)
´´

* Creamos la funcion de precision y la checamos 
´´
precision <- function(x){sum(diag(x)/(sum(rowSums(x)))) * 100}
precision(con_mat)
´´

