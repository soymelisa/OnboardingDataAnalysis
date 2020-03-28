library(tidyverse)
setwd('C:\Users\USER\SandBox\DataAnalysis\CursoDaraAnalysis\A2-Programacion-con-R\Sesion-07\Ejemplo-01')
mc_responses <- read.csv("multiple_choice_responses.csv")

#View(mc_responses)

pdf('ejemplo02.pdf', paper='USr', width=1000)

summ <- mc_responses %>% group_by(Q3) %>% summarise(users = length(Q3)) 

summ <- summ[order(-summ$users),]

summ %>% ggplot() +
  geom_bar(aes(x = reorder(Q3, users), y = users, fill=reorder(Q3, users)), stat = 'identity') +
  theme(axis.text.x = element_text(angle=65, vjust=0.6),legend.position = "right")

p <- summ[1:50,] %>% ggplot() +
  geom_bar(aes(x = reorder(Q3, users), y = users, fill=reorder(Q3, users)), stat = 'identity') 
p

p <- p + coord_flip()
p

p <- p +
  geom_text(aes(x = reorder(Q3, users), y = users,label=users), hjust=-0.1) +
  annotate("text", x = 31.1, y=750, label = "<- lugar 20!") +
  scale_fill_manual(values=c(rep('#8D8A89',30), "#208600",rep('#8D8A89',length(unique(mc_responses$Q3))-31))) + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6),legend.position = "none") +
  xlab('Top 50 paises')+
  ylab("Número de usuarios")

p

dev.off()
