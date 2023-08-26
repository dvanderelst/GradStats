population <- c(rnorm(n=10000, mean=2), rnorm(n=10000, mean=4.5))
den <- density(population)
plot(den, frame = TRUE, col = "black",main = "Population")

samp <- sample(population, size=25)

hist(samp, main='Sample')
