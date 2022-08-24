library(latex2exp)

# based on https://zhiyzuo.github.io/Pearson-Correlation-CI-in-Python/
rm(list = ls())
if (!is.null(dev.list()))
  dev.off()


library(latex2exp)
library(MASS)


n <- 10
population_correlation <- 0.25

sigma <-
  rbind(c(1, population_correlation), c(population_correlation, 1))
mu <- c(10, 5)
data <- mvrnorm(n = n, mu = mu, Sigma = sigma)
x <- data[, 1]
y <- data[, 2]
mean_x <- mean(x)
mean_y <- mean(y)

model <- lm(y ~ x)
mdl <- summary(model)
print(mdl)
aov <- anova(model)
print(aov)

#manual
residuals <- model$residuals
predicted <-predict(model)
SSB<- sum((predicted - mean(predicted)) ^ 2)
SSE<- sum(residuals ^ 2)

MSB <- SSB/1
MSE <- SSE/8

r2<-SSB/(SSB + SSE)
f <-MSB/MSE
r <-cor(x, y)




