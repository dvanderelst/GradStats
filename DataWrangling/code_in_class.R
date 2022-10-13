library(tidyverse)
library(readxl)
more_data <- read_excel("data/transit-data.xlsx", sheet = 'transport data', skip=1)
colnames(more_data) <- make.names(colnames(more_data))

some_columns <- select(more_data, sender.latitude, sender.longitude)

#data <- read_csv('data/pakistan_intellectual_capital.csv', n_max=10)
#colnames(data) <- make.names(colnames(data))

url <- 'https://raw.githubusercontent.com/dvanderelst/GradStats/main/DataWrangling/data/Titanic.csv'
Titanic <- read_csv(url)

filter_data <- filter(Titanic, Sex == 'male' & Age > 25 & Survived == 1)

filter_data <- filter(Titanic, Sex == 'male')
filter_data <- filter(filter_data, Age > 25)
filter_data <- filter(filter_data, Survived == 1)

filter_data <- filter(Titanic, Sex == 'female' & PClass =='1st')


depression_data <- read_tsv('data/raw_depression.csv')

suspected <- filter(depression_data, age > 120)


library(tidyverse)
library(haven)
demographics <- read_xpt('data/DEMO_J.XPT')
income <- read_xpt('data/INQ_J.XPT')
drugs <- read_xpt('data/DUQ_J.XPT')

drug_habits <- select(drugs, SEQN, DUQ200:DUQ280)
age<-select(demographics, SEQN, RIDAGEYR, RIDAGEMN)
finance <- select(income, SEQN, INDFMMPC,INDFMMPI, INQ300, IND235)


merged <- full_join(age, drug_habits, by='SEQN')
merged <- full_join(merged, finance, by='SEQN')
dim(merged)

merged1 <- full_join(age, drug_habits, by='SEQN')
merged2 <- right_join(age, drug_habits, by='SEQN')