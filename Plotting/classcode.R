library(tidyverse)

body_data <- read_csv('data/body.csv')

population1_color = '#d95f02'
population2_color = '#7570b3'


x <- 1:10
y1 <- runif(10) * x
y2 <- runif(10) * x

try(dev.off())
par(oma=c(0,0,0,0), mfrow = c(2,1))
x <- 1:10
y <- runif(10) * x

hist(body_data$ChestDepth, freq = FALSE, main ='A normalized histogram')
hist(body_data$Biiliac, freq = FALSE, main ='A normalized histogram')

par(oma=c(0,0,0,0), mfrow = c(1,1))
hist(body_data$Biiliac, freq = FALSE, main ='A normalized histogram')
