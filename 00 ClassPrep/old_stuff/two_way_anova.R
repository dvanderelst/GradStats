library(tidyverse)
library(equatiomatic)

data <- read_tsv('data/vik_table_12_2.csv')

result <- lm('score ~ sex * condition', data =data)
summary(result)

model.matrix(result)

interaction.plot(x.factor = data$sex, trace.factor = data$condition, response = data$score)