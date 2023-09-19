data(gala, package="faraway")
lmod <- lm(Species ~ Area + Elevation + Scruz + Nearest + Adjacent, gala)
plot(fitted(lmod),residuals(lmod),xlab="Fitted",ylab="Residuals")
abline(h=0)