rm(list = ls())
if(!is.null(dev.list())) dev.off()


data <- read.csv('data/body.csv')
hist(data$Waist, breaks = 25)

data <- read.csv('data/wages1833.csv')
plot(data$age, data$fwage)