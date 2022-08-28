rm(list = ls())
if(!is.null(dev.list())) dev.off()

library(latex2exp)

sample_size <- 31
pop_mean <- 15
pop_sd<-3

par(mfcol=c(1,2))

x <- seq(pop_mean - 3 * pop_sd, pop_mean + 3 * pop_sd, length=1000)
population <- dnorm(x, mean=15, sd = pop_sd)
plot(x, population, type='l',lty=3 ,lwd=3, xlab=TeX('Sample mean'), ylab = TeX('$\\Density$'), col='red')
t<-sprintf('Population distribution for \\mu = %i, \\sigma = %i', pop_mean, pop_sd)
title(TeX(t))

x <- seq(pop_mean - 3 * pop_sd, pop_mean + 3 * pop_sd, length=1000)
sampling <- dnorm(x, mean=15, sd = pop_sd/sqrt(sample_size))
plot(x, sampling, type='l', lwd=1, xlab=TeX('Sample mean'), ylab = TeX('$\\Density$'))
lines(x, population, lwd=3, add=TRUE, lty=3, col='red')
t<-sprintf('Sampling distribution for n = %i', sample_size, pop_mean, pop_sd)
title(TeX(t))
