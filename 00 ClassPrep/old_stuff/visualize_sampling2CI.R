rm(list = ls())
if(!is.null(dev.list())) dev.off()

library(latex2exp)

sample_mean <- 5
sample_sd <- 2
sample_size <- 15



x1 <- seq(-5, 5, length=1000)
x2 <-  seq(-10, 10, length=1000) * sqrt(sample_sd/sample_size)

y1 <- dt(x1, df = sample_size - 1)

plot(x1,y1,type='l', xlab = TeX('$t, \\bar{x} - \\mu$'), ylab='Density', col='blue')
lines(x2,y1,type='l', col='red')

label1<-TeX('$t = $\\bar{x} - \\mu / \\sqrt{S/N}$')
label2<-TeX('$\\bar{x} - \\mu = t \\times \\sqrt{S/N}$')
legend("topleft", legend=c(label1,label2), col=c('blue', 'red'), lty=1)

xx<-qt(0.025, df= sample_size-1)  * sample_sd / sqrt(sample_size)
print(xx)