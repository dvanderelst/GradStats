library(tidyverse)
car_data <- read_delim('data/cars.txt', delim = ' ')
grouped <- group_by(car_data, type, make)
summaries <- summarise(grouped, mean.length = mean(length))

wide <- pivot_wider(summaries, id_cols = make, names_from  = type, values_from = mean.length)
head(wide)



titanic <-read_csv('data/Titanic.csv', na = c('NA', '*'))
titanic <- filter(titanic, Age > 15)
grouped <- group_by(titanic, PClass, Sex)
# na.rm = TRUE removes NA values from the calculation
summaries <- summarise(grouped, mean.age = mean(Age, na.rm = TRUE))
survival <- summarise(grouped, proportion = mean(Survived), survivors = sum(Survived), total = length(Survived))
table <- pivot_wider(survival, id_cols = PClass, names_from = Sex, values_from = proportion)
table <- drop_na(table)
table <- mutate(table, diff = male - female)


