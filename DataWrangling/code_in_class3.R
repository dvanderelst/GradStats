library(tidyverse)
library(lubridate)
ss <- read_csv('data/ssadisability.csv')

longer_format <- pivot_longer(ss, cols=Oct_Total:Sept_Total, names_to = 'period_source', values_to = 'Count')
splitted <- separate(longer_format, period_source, into=c('Month', 'Source'), sep='_')
wider <- pivot_wider(splitted, names_from = 'Source', values_from = 'Count')
wider<-mutate(wider, Other = Total - Internet)
long_again <- select(wider, -Total)
long_again <- pivot_longer(long_again, cols = c(Internet, Other), names_to = 'Source', values_to = 'Count') 

numbers <- str_extract(long_again$Fiscal_Year, '[0-9]{2}')
numbers <- 2000 + as.integer(numbers)
long_again <- add_column(long_again, Year = numbers)
long_again <- select(long_again, -Fiscal_Year)

long_again <- mutate(long_again, correction =  Month %in% c('Oct', 'Nov', 'Dec'))
long_again <- mutate(long_again, Year = Year - correction)

long_again$date <- paste('01', long_again$Month, long_again$Year)
long_again$date <-dmy(long_again$date)

coal_data <- read_csv('data/coal.csv', skip=2, na = "--")
colnames(coal_data)

existing_names <- colnames(coal_data)
existing_names[1] <- 'country'
colnames(coal_data) <- existing_names

colnames(coal_data)
long_format <- pivot_longer(coal_data, names_to = 'year', values_to = 'coal_use', cols = '1980':'2009')


regions <- c("North America", "Central & South America", "Antarctica", "Europe", "Eurasia", "Middle East", "Africa", "Asia & Oceania", "World")

long_format <- mutate(long_format, is_region =long_format$country %in% regions)

region_data <- filter(long_format, is_region)
country_data <- filter(long_format, !is_region)

# Remove the 'is_region' column from both tibbles
region_data <- select(region_data, -is_region)
country_data <- select(country_data, -is_region)
