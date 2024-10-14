library(tidyverse)
library(skimr)
url<-'data/pizzasize.csv'
data <- read_csv(url)
data <- mutate(data, Area = pi * (Diameter/2)^2)


data <- read_delim('data/cars.txt', delim = ' ')
data <- mutate(data, surface = length * width)
data <- mutate(data, large_car = ifelse(surface > 14000, 'large', 'small'))

#case_when(mpg > 30 ~ 'high', mpg > 20 ~ 'medium', mpg <= 20 ~ 'low')



data <- mutate(data, efficiency_category = case_when(mpg_city > 30 ~ 'high',
                                                     mpg_city >= 20 ~ 'medium',
                                                     mpg_city <= 25 ~ 'low'))


# Exercise 1
# Read in the cars.txt file
# Print the first lines of the data
# Print the column names to screen
# Calculate the difference in mpg on the highway and the city, add this difference as a new variable to the data.

data <- read_delim('data/cars.txt', delim = ' ')
print(head(data))

data <- mutate(data, mpg_diff = mpg_hgw - mpg_city)

# Exercise 2
# Read the wages1833.csv data file (from the data folder).
# Add a new variable that lists the difference between the number of male and female workers
# Adds a new variable diff_pct that gives the difference in average wage between the male and female workers expressed as a percentage of the female wage. The diff_pct will give a positive number if males earn more on average, and a negative number if females earn more.

data <- read_csv('data/wages1833.csv')
data <- mutate(data, diff_pct = 100 * (mwage - fwage) / fwage)

