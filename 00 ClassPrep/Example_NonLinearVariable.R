data<-read.csv('data/vik_table_9_2.csv')

data$Y2<-data$X1 ** 3
data$X13<-data$X1**3


model1<-lm(Y2~X1, data=data)
model2<-lm(Y2~X13, data=data)

plot(data$X1,data$Y2)

coef1<-model1$coefficients
coef2<-model2$coefficients

x_values<-0:11

predict1 <- coef1[1] + coef1[2] * x_values
predict2 <- coef2[1] + coef2[2] * x_values ** 3

points(x_values, predict1, type='l', col='red')
points(x_values, predict2, type='l', col='green')

summary()

