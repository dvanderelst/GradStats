rm(list = ls())
if(!is.null(dev.list())) dev.off
library(latex2exp)

assumed_population_mean <- 5
assumed_population_sd <- 1
sample_size <- 25

# construct theoretical sampling distribution
se_sampling_distribution <- assumed_population_sd / sqrt(sample_size)
mn_sampling_distribution <- assumed_population_mean

xi <- seq(-2 + assumed_population_mean, 2 + assumed_population_mean, length=1000)
yi <- dnorm(xi, mean=mn_sampling_distribution, sd = se_sampling_distribution)
plot(xi,yi,type='l', xlab = TeX('Sample mean, $\\bar{x}$'), ylab='Density')

# sample_distribution_mean <- mean(population)
# sample_distribution_sd <- sd(population) / sqrt(sample_size)
# x <- seq(min(sample_means), max(sample_means), length=1000)
# y <- dnorm(x, mean=sample_distribution_mean, sd=sample_distribution_sd)
# 
# plot(density(sample_means))
# lines(x, y, lwd=3, lty=2)
# abline(v=population_mean, lwd=3, lty=2)