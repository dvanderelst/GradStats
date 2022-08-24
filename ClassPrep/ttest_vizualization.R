rm(list = ls())
if(!is.null(dev.list())) dev.off()

sample_size <- 15

population1 <- rnorm(100000, mean = 7.5, sd = 2)
population2 <- rnorm(100000, mean = 5.7, sd = 2)
hist(population1, breaks=100, col=rgb(1,0,0,0.1), main='', xlab = 'Penguin Weight')
hist(population2, breaks=100,  add=TRUE, col=rgb(0,0,1,0.1))
title('Population 1 and 2')

sample1 <- sample(population1, sample_size)
sample2 <- sample(population2, sample_size)

hist(sample1, breaks=100, col=rgb(1,0,0,0.1), main='')
hist(sample2, breaks=100,  add=TRUE, col=rgb(0,0,1,0.1))
title('Population 1 and 2')

