
library(sjPlot)
#library(MASS)

f_values<-c()
repeats <- 10000
n <- 15

#Set all to zero to get the F value under the null hypothesis
beta1 <- 0
beta2 <- 0
beta3 <- 0

for (x in 1:repeats){
  
  x1 <- rnorm(n, mean = 0, sd = 1)
  x2 <- rnorm(n, mean = 0, sd = 1)
  x3 <- rnorm(n, mean = 0, sd = 1)
  dependent <- beta1 * x1 + beta2 * x2 + beta3 * x3 + rnorm(n, mean = 0, sd = 1)
  model<-lm(dependent~x1 + x2 + x3)
  sm<-summary(model)
  f_value <-sm$fstatistic[1]
  f_values<-c(f_values, f_value)
}


hist(f_values,probability=TRUE,breaks=100)


sm<-summary(model)
sm