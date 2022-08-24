rm(list = ls())
if(!is.null(dev.list())) dev.off()

library(latex2exp)

sample_size <- 100
sample_r <-0.25

x1 <- seq(-3, 3, length=1000)
x2 <-  x1 / sqrt(sample_size + x1^2 -2)

y1 <- dt(x1, df = sample_size - 2)

plot(x1,y1,type='l', xlab = TeX('$t, \\r - \\rho$'), ylab='Density', col='blue')
lines(x2,y1,type='l', col='red')


t <-qt(0.025, df= sample_size-2)

xx<-t/ sqrt(sample_size + t^2 - 2)
lower <-sample_r+xx
upper <- sample_r - xx