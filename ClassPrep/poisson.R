library(latex2exp)
library(faraway)
#P(k goals in a World Cup soccer match) - wikipedia
prop<-c(0.082, 0.205, 0.257, 0.213, 0.133,0.067,0.028, 0.010)
goals<-c(0,1,2,3,4,5,6,7)

lambda <- weighted.mean(goals, prop)

plot(goals, dpois(goals, lambda=lambda), type='l', col='red', lwd=3, main = "P(k goals in a World Cup soccer match)")
points(goals, prop, type = 'b')
text(5, 0.2,  TeX("$\\lambda$ = 2.475"),
     cex=3, pos=3,col="red")

####SIMULATION

ice_lambda <- 5
stone_lambda <- 10
sample_size<-150
bins<-20
col1 = rgb(0,0,1,1/4)
col2 = rgb(1,0,0,1/4)

ice <- rpois(sample_size, ice_lambda)
stone <- rpois(sample_size, stone_lambda)

p1 <- hist(ice, breaks = seq(-0.5,35.5), freq=F, ylim = c(0, 0.3), col=col1, xlab='counts')                
p2 <- hist(stone, breaks = seq(-0.5,35.5), freq=F, ylim = c(0, 0.3), add=T, col=col2)         

x_values <- seq(0,25)
points(x_values, dpois(x_values, lambda=ice_lambda), type='b', col='blue', lwd=3)
points(x_values, dpois(x_values, lambda=stone_lambda), type='b', col='red', lwd=3)

#%%
classes <- c(rep(1,sample_size), rep(2,sample_size))
data <- c(ice, stone)

m1 <- glm(data ~ factor(classes), family="poisson")
summary(m1)

###############PG 97
data <-read.csv('data/fHH1.csv')
model1 <- glm(total ~ age, family = poisson, data = data)
summary(model1)
coefficients <- model1$coefficients

age1<-55
age2<-52

prediction1 <- exp(coefficients[1] + age1 * coefficients[2])
prediction2 <- exp(coefficients[1] + age2 * coefficients[2])
#####################
data <-read.csv('data/poisson_sim.csv')
model2 <- glm(num_awards ~ math, family = poisson, data = data)
summary(model2)
