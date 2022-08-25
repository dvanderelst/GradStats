prop_black_swans <- 0.75
sample_size = 10
x <-c(0:10)

h<-sprintf("Population: %.2f percent black swans, sample size: %i", prop_black_swans * 100, sample_size)
y <- dbinom(x, size=sample_size, prob=prop_black_swans)
barplot(y, names.arg = x, xlab='Number of black swans', ylab = 'probability')
title(h)