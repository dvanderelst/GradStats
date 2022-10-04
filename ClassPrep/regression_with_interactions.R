library(tidyverse)
library(equatiomatic)

data <- as_tibble(state.x77)
colnames(data) <- make.names(colnames(data))


data <- mutate(data, Area1 = Area - mean(Area))
data <- mutate(data, Illiteracy1 = Illiteracy - mean(Illiteracy))

data<-mutate(data, cross = Area * Illiteracy)
data<-mutate(data, cross_zeroed = Area1 * Illiteracy1)

selected <- select(data, c(Income,Area,Illiteracy,Area1,Illiteracy1,cross,cross_zeroed))

cor(selected)

result1a <- lm('Income~Area + Illiteracy', data = data)
summary(result1a)

result1b <- lm('Income~Area * Illiteracy', data = data)
summary(result1b)

result2a <- lm('Income~Area1 + Illiteracy1', data = data)
summary(result2a)

result2b <- lm('Income~Area1 * Illiteracy1', data = data)
summary(result2b)

print(result1a)
print(result1b)
print(result2a)
print(result2b)

# data<-mutate(data, cross = X1 * X2)
# data<-mutate(data, cross_zeroed = NX1 * NX2)
# 
# cor(data)


# states <- mutate(states, Murder1 = Murder - mean(Murder))
# states <- mutate(states, Income1 = Income - mean(Income))
# states <- mutate(states, Illiteracy1 = Illiteracy - mean(Illiteracy))
# states <- mutate(states, inter = Illiteracy * Murder)
# states <- mutate(states, inter1 = Illiteracy1 * Murder1)
# 
# result <- lm('Income~Murder * Illiteracy', data = states)
# s <- select(states, c(Income, Murder, Illiteracy, inter))
# summary(result)
# 
# 
# result1 <- lm('Income~Murder1 * Illiteracy1', data = states)
# s1 <- select(states, c(Income, Murder1, Illiteracy1, inter1))
# summary(result1)
# 
# result1b <- lm('Income~Murder1 + Illiteracy1', data = states)
# s1 <- select(states, c(Income, Murder1, Illiteracy1, inter1))
# summary(result1b)
# 
# 
# 
# par(mfrow=c(1,2))
# 
# plot(states$Murder, states$Income)
# plot(states$Murder1, states$Income1)
# 
# par(mfrow=c(1,1))
# plot(states$Murder * states$Income, states$Murder1* states$Income1)
# 
# pairs(s)
# pairs(s1)
