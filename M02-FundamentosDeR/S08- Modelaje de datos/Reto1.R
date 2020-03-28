## Regresión lineal

head(mtcars)
# creamos un scatter.smoothpara ver la relación peso/millas
scatter.smooth(x=mtcars$wt, y=mtcars$mpg, main="relación peso y millas por galón")  

# paso 2. correlación entre variables
cor(mtcars$wt, mtcars$mpg) 

# creamos el modelo lineal
modlin <- lm(wt ~ mpg, data=mtcars)  
print(modlin)
summary(modlin)
