library(reshape)
library(ggplot2)

rm(list = ls())
if(!is.null(dev.list())) dev.off()

sample_size <- 15

population1 <- rnorm(100000, mean = 7.5, sd = 2)
population2 <- rnorm(100000, mean = 10, sd = 2)
population3 <- rnorm(100000, mean = 6, sd = 2)


hist(population1, breaks=100, col=rgb(1,0,0,0.2), main='', xlab = 'Penguin Weight')
hist(population2, breaks=100,  add=TRUE, col=rgb(0,1,0,0.2))
hist(population3, breaks=100,  add=TRUE, col=rgb(0,0,1,0.2))
title('Populations 1, 2, and 3')

france <- sample(population1, sample_size)
senegal <- sample(population2, sample_size)
japan <- sample(population3, sample_size)

hist(france, breaks=100, col=rgb(1,0,0,0.2), main='', xlab='Penguin Weight')
hist(senegal, breaks=100,  add=TRUE, col=rgb(0,1,0,0.2))
hist(japan, breaks=100,  add=TRUE, col=rgb(0,0,1,0.2))
title('Samples 1, 2, and 3')

data <-data.frame(cbind(france,senegal,japan))
data<-melt(data)
colnames(data) <- c('sample', 'y')
data$sample<-factor(data$sample)

model <- lm(data$y ~ data$sample)

print(summary(model))


p <- ggplot(data=data, aes(x=sample, y=y))+
  geom_jitter(aes(x=sample, y=y), position = position_jitter(width = 0.05))+
  stat_summary(fun=mean, colour="red", geom="point", size=10)
print(p)


print(model$contrasts)
print(contr.treatment(3))

## Demo: anova with 2 levels == t-test
data <-data.frame(cbind(senegal,japan))
data<-melt(data)
colnames(data) <- c('sample', 'y')
data$sample<-factor(data$sample)

model <- lm(data$y ~ data$sample)

print(summary(model))

print(t.test(senegal, japan, var.equal = TRUE))