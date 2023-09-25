data <- read.csv('data/body.csv')
x <- data$ChestDepth
y <- data$ChestDia

plot(x,y)