
## Programacion orientada a objetos  

### OBJETIVO
- Importación de un dataset
- Cambiar los valores de un objeto

#### REQUISITOS
1. Contar con R studio.
1. Usar la carpeta de trabajo `Sesion02/Reto-01`

#### DESARROLLO
Importamos el dataset de **Spotify**, desplegaremos su estructura e identifiaremos la variable del tiempo que se encuentra en **ms** , se realizaran las operaciones necesarias para convertir el valor a **minutos**

# Estructura
str(spotify)

# Cambio de duración a minutos
spotify <- transform(spotify, duration_ms = duration_ms / 1000 / 60)

# 
str(spotify)


