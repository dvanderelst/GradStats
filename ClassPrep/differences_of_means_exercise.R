sample_size<-12
population_men_mean <- 4
population_women_mean <- 5
sd_population <- 1.5


differences <-c()
p_values<-c()
for (i in 1:100000)
{
  men <- rnorm(sample_size, mean = population_men_mean, sd=sd_population)
  women <- rnorm(sample_size, mean = population_women_mean, sd=sd_population)
  mean_men <- mean(men)
  mean_women <- mean(women)
  difference <-mean_women - mean_men
  differences <- c(differences, difference)
}

sampling_distribution_mean<- population_women_mean - population_men_mean

sample_sd <- sd_population / sqrt(sample_size)
sampling_distribution_sd <- sqrt(sample_sd^2 + sample_sd^2)

x <- seq(-2, 2, length=1000)
y <- dnorm(x, mean =  sampling_distribution_mean, sd = sampling_distribution_sd)
  
hist(differences, freq=F,breaks=50, main='simulated and calculated sampl. dist.')
points(x,y, t='l')


simulated_p <- mean(differences > 1.5)

