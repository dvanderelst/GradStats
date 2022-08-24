rm(list = ls())
if(!is.null(dev.list())) dev.off()

library(latex2exp)

sample_size <- 25
assumed_mean <- 30
real_mean <- 25

# A population of blue whales. We can not observe this.
population <- rnorm(1000000, mean=assumed_mean, sd=assumed_mean/2)
plot(density(population), xlab='whale length', main='The population distribution')

# Let's pull a sample
sampled <- rnorm(sample_size, mean=real_mean, sd=real_mean/2)
hist(sampled,xlab='whale length', main='Our sample')

#Based on our sample, let's construct the sampling distribution
#We don't know the population sigma. So, we'll use the t-distribution

x <- seq(-5, +5, length=1000)
y <- dt(x, df=sample_size-1)
plot(x, y, type='l', xlab=TeX('$(\\bar{X} - \\mu$)/(S/\\sqrt{N})$'))
title(TeX('Sampling distribution: likelihood for values $(\\bar{X} - \\mu$)/(S/\\sqrt{N})$'))

#Let's add our observation to the figure 
# and the 95% boundaries
plot(x, y, type='l', xlab=TeX('$(\\bar{X} - \\mu$)/(S/\\sqrt{N})$'))
title(TeX('Sampling distribution: likelihood for values $(\\bar{X} - \\mu$)/(S/\\sqrt{N})$'))
tvalue <- (mean(sampled) - assumed_mean) / (sd(sampled)/sqrt(sample_size))
pvalue <- 2 * (1 - pt(abs(tvalue), df=sample_size-1))

print(tvalue)
print(pvalue)

abline(v=tvalue, col='red')

lower <-qt(0.025, df=sample_size-1)
upper <-qt(1- 0.025, df=sample_size-1)
abline(v=lower)
abline(v=upper)



# Let's do the whole thing in 1 line
result <- t.test(sampled, mu=assumed_mean)
print(result)
