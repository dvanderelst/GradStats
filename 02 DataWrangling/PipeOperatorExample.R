library(tidyverse)
data <- runif(10)
differences <- diff(data)
mn_differences <- mean(differences)

result <- data %>% diff() %>% mean()
