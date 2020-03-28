library(tidyverse)
library(waffle)
library(magrittr)
library(hrbrthemes)

setwd('C:\Users\USER\SandBox\DataAnalysis\CursoDaraAnalysis\A2-Programacion-con-R\Sesion-07\Ejemplo-01')
mc_responses <- read.csv("multiple_choice_responses.csv")

pdf('ejemplo01.pdf', paper='USr', width=1000)

ggplot(data = mc_responses, aes(x = Q2, fill = Q2)) +
  geom_bar() +
  scale_fill_manual(values=rainbow(4)) + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6),legend.position = "right") +
  xlab('Genero')+
  ylab("Número de usuarios") +
  ggtitle ('Distribucion por genero') +
  labs(fill='Genero')
#+
#  theme_minimal()

ggplot(data = mc_responses, aes(x = Q1, fill = Q1)) +
  geom_bar() +
  scale_fill_manual(values=rainbow(11)) + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6),legend.position = "right") +
  xlab('Edades')+
  ylab("Número de usuarios") +
  ggtitle ('Distribucion por edad') +
  labs(fill='Edades')
#+
#theme_minimal()

ggplot(data = mc_responses, aes(x = Q1, fill = Q2)) +
  geom_bar() +
  facet_wrap(~Q2, scales = 'free_y')+
  scale_fill_manual(values=rainbow(4)) + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6),legend.position = "none") +
  xlab(element_blank())+
  ylab('numero de usuarios')

dev.off()
