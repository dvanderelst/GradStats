# based on https://zhiyzuo.github.io/Pearson-Correlation-CI-in-Python/
rm(list = ls())
if(!is.null(dev.list())) dev.off()


library(latex2exp)
library(MASS)


n <- 10
population_correlation <- 0.25

sigma <- rbind(c(1, population_correlation), c(population_correlation, 1))
mu <- c(10, 5)
data <- mvrnorm(n = n, mu = mu, Sigma = sigma)
x <- data[, 1]
y <- data[, 2]
mean_x <- mean(x)
mean_y <- mean(y)

r <- cor(x, y)

plot(x, y)
abline(v = mean_x, lty = 3)
abline(h = mean_y, lty = 3)


# Under the assumption that r == 0, the following variable follows a t-distribution
# with dof = n -2
t <- r * sqrt((n - 2) / (1 - r ^ 2))
print('t:')
print(t)

curve(dt(x, df = n - 2), from = -4, to = 4, xlab = TeX('$r \\times \\sqrt{(n-2)/(1-r^2)}$'))

curve(dt(x, df = n - 2), from = -4, to = 4, xlab = TeX('$r \\times \\sqrt{(n-2)/(1-r^2)}$'))
abline(v=r, lw=3, lty=3, col='red')


# This can be used to test the hypothesis that r = 0

# The confidence intervals are determined via the fisher transform to
# make sure they are bounded

curve(dnorm(x, mean= population_correlation, sd = 1/sqrt(n-3)), from = -4, to = 4, xlab = TeX('$F(r)'), ylab='density')
abline(v=population_correlation, lty=3)

curve(dnorm(x, mean= 0, sd = 1/sqrt(n-3)), from = -4, to = 4, xlab = TeX('$F(r) - F(\\rho)'), ylab='density')
abline(v=0, lty=3)

se <- 1 / sqrt(length(x) - 3)
transformed_r <- atanh(r)

lower <- tanh(transformed_r + qnorm(0.025) * se)
upper <- tanh(transformed_r + qnorm(0.975) * se)

print('interval:')
print(lower)
print(upper)

# Let's use the fisher transform approach to calculate the P-value
# This is NOT how R does this (at least not per default?)
# But it will be approximate the method used by R (which is based on the t-distribution)

z_value <-  transformed_r / se
p_value_using_tranform <- 2*pnorm(q=z_value, lower.tail=FALSE)
print('p_value_using_tranform')
print(p_value_using_tranform)

# R's default
print(cor.test(x, y))