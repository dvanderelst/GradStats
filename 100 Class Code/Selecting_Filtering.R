library(tidyverse)
library(readxl)
data <- read_excel("data/transit-data.xlsx", sheet = 'transport data', skip=1)
colnames(data) <- make.names(colnames(data))

subset <- select(data, date, sender.latitude)

# Select variables ending with a integer using regular expressions
# This should only return the one variable that R made while reading in the data
subset <- select(titanic_data, matches("[0-9]$"))


# Exercise 1
titanic_data <- read_csv("data/Titanic.csv")
#Count the number of male survivors that were older than 25.
copilot <- filter(titanic_data, Sex == "male", Age > 25, Survived == 1)
my_try <- filter(titanic_data, Sex == "male" & Age > 25 & Survived == 1)

#How many first class passengers were female?
female_first_class <- filter(titanic_data, PClass == '1st' & Sex == 'female')
male_third_class <- filter(titanic_data, PClass == '3rd' & Sex == 'male')

#How many female passengers survived?
female_first_class_survived <- filter(titanic_data, PClass == '1st' & Sex == 'female' & Survived == 1)
male_third_class_survived <- filter(titanic_data, PClass == '3rd' & Sex == 'male' & Survived == 1)

# Exercise 2
car_data <- read_delim("data/cars.txt", delim = " ")



