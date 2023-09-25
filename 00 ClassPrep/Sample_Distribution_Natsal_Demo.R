library(tidyverse)
library(ggplot2)

data<-read_csv('Natsal.csv')
data<-filter(data,number<9995)
data$lg <-log10(data$freq)

#plot(data$number, lg, xlab = 'Sexual Partners', ylab = 'Frequency', type='l')

p <- ggplot(data, aes(number, lg)) + 
  geom_smooth(method = "loess", se = FALSE) +
  labs(y = "Frequency (Log10)", x = "Number of sexual partners")
p

sampled <-sample(data$number, size=1000, replace=TRUE, prob=data$freq)

hist(sampled)