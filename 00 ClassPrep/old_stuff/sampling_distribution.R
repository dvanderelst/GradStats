rm(list = ls())
if(!is.null(dev.list())) dev.off
library(latex2exp)

sample_size <- 25

# Create a population with known attributes
population_mean <- 5
population <- rnorm(1000000, mean=population_mean, sd=1)
hist(population, 50, xlab = 'Weight of penguin')
abline(v=population_mean, lty=3, lw=5, col='red')

# Get a single sample
sampled <- sample(population, sample_size)
hist(sampled, xlab = 'Weight of sampled penguin')

# Sample the population many times 

sample_means <- c()
for (i in 1:10000)
{
  sampled <- sample(population, sample_size)
  sample_mean <- mean(sampled)
  sample_means <- c(sample_means, sample_mean)
}

# Visualize the distribution of sample means

hist(sample_means, 50, xlab='Sample mean')


# Use equations to construct sampling distribution for the mean

sample_distribution_mean <- mean(population)
sample_distribution_sd <- sd(population) / sqrt(sample_size)
x <- seq(min(sample_means), max(sample_means), length=1000)
y <- dnorm(x, mean=sample_distribution_mean, sd=sample_distribution_sd)

plot(density(sample_means))
lines(x, y, lwd=3, lty=2)
abline(v=population_mean, lwd=3, lty=2)
