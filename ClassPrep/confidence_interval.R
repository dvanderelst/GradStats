library(latex2exp)
# Create a population with known attributes
population <- rnorm(1000000, mean=100, sd=10)
population_mean <- mean(population)
sample_size <- 150

# Use equations to construct sampling distribution for the mean

sample_distribution_mean <- mean(population)
sample_distribution_sd <- sd(population) / sqrt(sample_size)
x <- seq(population_mean-5, population_mean+5, length=1000)
y <- dnorm(x, mean=sample_distribution_mean, sd=sample_distribution_sd)

plot(x, y, type='l', lwd=1, xlab=TeX('$\\bar{x}$'), ylab = TeX('$\\Density$'))
abline(v=population_mean, lwd=1, lty=2)
title(TeX('Sampling distribution of the mean'))

# Shift the sampling distribution to get the range of likely errors

plot(x - population_mean, y, type='l', lwd=1, xlab=TeX('$\\bar{x} - \\mu$'), ylab = TeX('$\\Density$'))
abline(v=0, lwd=1, lty=2)
title(TeX('Distribution of $\\bar{x}- \\mu$'))

# Normalize the sampling distribution (this is the z-distribution)

x_values <- (x - population_mean) / sample_distribution_sd

plot(x_values, y, type='l', lwd=1, xlab=TeX('$\\bar{x} - \\mu$, Units: $\\frac{\\sigma}{\\sqrt{N}}$'), ylab = TeX('$\\Density$'))
abline(v=0, lwd=1, lty=2)
title(TeX('Distribution of $\\bar{x}- \\mu$ (Standardized))'))

# Get the 95% range of errors

x <- seq(-5, +5, length=1000)
y <- dnorm(x, mean=0, sd=sample_distribution_sd)
a <-qnorm(0.025, mean=0, sd=sample_distribution_sd)
b <-qnorm(1- 0.025, mean=0, sd=sample_distribution_sd)

plot(x, y, type='l', lwd=1, xlab=TeX('$\\bar{x} - \\mu$'), ylab = TeX('$\\Density$'))
abline(v=a, lwd=1, lty=2)
abline(v=b, lwd=1, lty=2)
title(TeX('95% range of errors'))
print(a)
print(b)

