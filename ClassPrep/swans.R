rm(list = ls())
if(!is.null(dev.list())) dev.off
library(latex2exp)

prop_black_swans <- 0.75
sample_size = 10
x <-c(0:10)

h<-sprintf("Population: %.2f percent black swans, sample size: %i", prop_black_swans * 100, sample_size)
y <- dbinom(x, size=sample_size, prob=prop_black_swans)
barplot(y, names.arg = x, xlab='Number of black swans', ylab = 'probability')
title(h)


prop_black_swans <- 0.5
sample_size = 15
found <-5
x <-c(0:sample_size)

mask <- rep(0, sample_size + 1)
mask[found+1]<-1
h<-sprintf("Population: %i percent black swans, sample size: %i", prop_black_swans * 100, sample_size)
y <- dbinom(x, size=sample_size, prob=prop_black_swans)
barplot(y, names.arg = x, xlab='Number of black swans', ylab = 'probability')
#barplot(y * mask, names.arg = x, col='red', add=TRUE)
title(h)

cbind(x, round(y*100))

h<-sprintf("Population: %i percent black swans, sample size: %i", prop_black_swans * 100, sample_size)
y <- dbinom(x, size=sample_size, prob=prop_black_swans)
barplot(y, names.arg = x, xlab='Number of black swans', ylab = 'probability')
barplot(y * mask, names.arg = x, col='red', add=TRUE)
title(h)


