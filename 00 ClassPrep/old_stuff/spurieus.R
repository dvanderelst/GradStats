cheese <- c(54,46,42,50,43,41,46,39,37,45,45,41,54)
sheets <-c(601,579,572,617,566,547,597,580,536,579,576,601,664)

model <-lm(sheets~cheese)

plot(cheese, sheets, xlab='Predictor X', ylab='Data or dependent variable Y')
abline(model, col='red', lwd=3, lty=3)
abline(h=mean(sheets), col='blue', lwd=3, lty=3)
cor.test(cheese, sheets)

summary(model)
anova(model)