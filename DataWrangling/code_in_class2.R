library(tidyverse)
library(readxl)

library(gapminder)
gap_data <- gapminder

# Filter the data for the Americas in 2007. Select only the lifeExp variable and deselect all other variables.
result1 <- filter(gap_data, continent == 'Americas' & year == 2007)
result1 <- select(result1, lifeExp)

## Alternative (using base R)
result1b <- subset(gap_data, continent == 'Americas' & year == 2007, lifeExp)

# Create the variable gdp, defined as the product of pop and gdpPercap.
gap_data <- mutate(gap_data, gdp = (gdpPercap * pop)/1000000)

# Identify the observation (combination of country, continent, and year) with lowest gdp per person.
result2 <- arrange(gap_data, gdpPercap)
result2 <- result2[1, ]

# Identify all observations with above average life expectancy, stratified for each continent.
grouped <- group_by(gap_data, continent, year)
avgs <- summarise(grouped, avg = mean(lifeExp))
merged<- left_join(gap_data, avgs, by =c('continent', 'year'))
merged<- mutate(merged, higher = lifeExp > avg)
result3 <- filter(merged, higher)

# Compute the mean life expectancy for each year per continent.