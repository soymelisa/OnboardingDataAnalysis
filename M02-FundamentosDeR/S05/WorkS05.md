#Ejemplo de una función
mi_funcion <- function(c,b,a){
  paso.1 <- (a+b)*4 + 2*a
  paso.2 <- paso.1**2 + c/2
  paso.3 <- paso.2**3

  return(paso.3)
}

# Crear un dataframe para pruebas
library(dplyr)
Titanic <- Titanic %>% data.frame() 

# Ejemplo dplyr
Titanic %>% filter(Class == '1st') %>% select(Freq) %>% View()

#Ejemplo de SQL
#select Freq, CONCAT(Class, Sex) as classex, LIT('NUEVO VALOR') as new
#from Titanic
#where Class = '1st'

# Ejemplos mutate
Titanic %>% mutate(classex = paste(Class,Sex,sep='-')) %>% View
Titanic %>% mutate(freq_10 = Freq / 10) %>% View

## Ejemplo1

ej1 <- function(cadenita){
  return(paste(cadenita,'lo nuevo')) # esto es un objeto string
}

nueva_cadena <- ej1('Diego') 

nueva_cadena

ej2 <- function(cadenita){
  print(paste(cadenita, 'esto es algo nuevo'))
}

nueva_cadena2 <- ej2('Diego')

saludo <- function(nombre){
  mensaje <- paste('Hola', nombre)
  return(mensaje)
}

#Reto 2
data <- read.csv("Metro_Interstate_Traffic_Volume.csv")
str(data)
niveles.orden <- sort(levels(data$weather_main))
data$weather_main_orderer <- factor(x = data$weather_main, levels = niveles.orden, ordered = TRUE)

#Reto03
df.traffic.filter %>% group_by(clima)%>%
  min(trafico) %>%
  max(trafico)
  ####
  
  

#Reto 3

#reto 3
mean.traffic <- df.traffic$traffic_volume %>% mean
df.traffic.filter <- df.traffic %>% 
  rename(clima=weather_main,trafico=traffic_volume) %>% 
  filter(trafico >= mean.traffic)

df.traffic.grouped <- df.traffic.filter %>%
  group_by(clima) %>% 
  summarise(min_tr = min(trafico), max_tr = max(trafico), mean_trafic = mean(trafico)) 

df.traffic.grouped %>% 
  mutate(max_min = max_tr - min_tr)
  
  
#Sesion 6
#Reto 1

mpg %>% group_by(manufacturer) %>% summarise(cuantos=length(manufacturer))

+ theme(axis.text.x = element_text(angle = 90, hjust = 1))

# 

graphic1 <- mpg %>% group_by(manufacturer) %>% summarise(cuantos=length(manufacturer))
ggplot(graphic1) +
  geom_bar(stat='identity', aes(x=manufacturer, y= cuantos)) +  
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

##

mpg %>% group_by(manufacturer) %>% summarise(cuantos=length(manufacturer)) %>% 
  ggplot() +
  geom_bar(stat='identity', aes(x=manufacturer, y= cuantos)) +  
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggplot(mpg) +
  geom_bar(stat='count', aes(x=manufacturer)) +  
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

aes(x=reorder(Age, sort(as.numeric(Age))))

#reto 06 -	02
ggplot(usaplayers, aes(x=Age)) +
  geom_bar()

ggplot(usaplayers, aes(x=as.numeric(Age))) +
  geom_bar()

# reorder se utiliza con sort como número en vez de 
ggplot(usaplayers, aes(x=reorder(Age, sort(as.numeric(Age))))) +
  geom_bar()
  
#reto 3
nba %>% filter(Nationality %in% c('Mexico', 'Canada','Brazil')) %>%
  ggplot()+
  geom_density(aes(x=Weight))+
  facet_wrap(~Nationality)

nba %>% filter(Nationality %in% c('Mexico', 'Canada','Brazil')) %>% 
  ggplot()+
  geom_density(aes(x=Weight,color=Nationality))
