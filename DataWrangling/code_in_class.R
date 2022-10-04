library(tidyverse)
library(readxl)
more_data <- read_excel("data/transit-data.xlsx", sheet = 'transport data', skip=1)
colnames(more_data) <- make.names(colnames(more_data))

data <- read_csv('data/pakistan_intellectual_capital.csv', n_max=10)
colnames(data) <- make.names(colnames(data))