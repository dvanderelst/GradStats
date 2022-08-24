rm(list = ls())
if(!is.null(dev.list())) dev.off()

library(latex2exp)
# Create a population with known attributes
population <- rnorm(1000000, mean=100, sd=10)
population_mean <- mean(population)
sample_size <- 10

sampled <- sample(population, sample_size)

# Use equations to construct sampling distribution for the mean
x <- seq(-5, +5, length=1000)
y <- dt(x, df=sample_size-1)

# Get the 95% range of errors
a <-qt(0.025, df=sample_size-1)
b <-qt(1- 0.025, df=sample_size-1)

# plot distribution and interval
        
plot(x, y, type='l', lwd=1, xlab=TeX('$\\bar{x} - \\mu$, units: $S/\\sqrt{n}$'), ylab = TeX('$\\Density$'))
abline(v=population_mean, lwd=1, lty=2)
abline(v=a, lwd=1, lty=2)
abline(v=b, lwd=1, lty=2)
title(TeX('Distribution of $\\bar{x} - \\mu$'))

units <- sd(sampled)/sqrt(sample_size)
lower <-a * units
upper <-b * units

#double check
r <- t.test(sampled)
delta <- r$conf.int[2]-mean(sampled)


