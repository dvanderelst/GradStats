
xi <- seq(from=0, to=10, length.out=1000)
dist1 <- dnorm(xi, mean = 5)
dist2 <- dnorm(xi, mean = 5+2)

par(mfrow=c(1,2))
plot(xi, dist1, type='l', col='red', lwd=4, lty=1, main = 'Null hypothesis', xlab = 'penguin_weight')
lines(xi, dist1, col='blue', lwd=4, lty=3)

plot(xi, dist1, type='l', col='red', lwd=4, lty=1, main = 'Alternative hypothesis', xlab = 'penguin_weight')
lines(xi, dist2, col='blue', lwd=4, lty=1)

sample1 <- rnorm(15, mean = 5)
sample2 <- rnorm(15, mean = 5+2)

my_red <- adjustcolor( "red", alpha.f = 0.25)
my_blue <- adjustcolor( "blue", alpha.f = 0.25)

par(mfrow=c(1,1))
breaks <-seq(0:10)
prop <- hist(sample1, col=my_red, main = 'Histogram of damples', breaks=breaks)
hist(sample2, add=TRUE, col = my_blue, breaks=breaks)
