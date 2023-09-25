population <- c(12,34,69,36,13,47,98,12,18,87,65,42,98,76,34,18,10,89,90,78,65,53,27,57,69,23,44,12,67,11,15)

statistics <-c()
sample_size <-5

for (x in 1:10000)
  {
  sampled <- sample(population, sample_size)
  statistic <- mean(sampled)
  statistics<-c(statistics, statistic)
  
  sample_part <- noquote(toString(sampled))
  result_part<- noquote(toString(statistic))
  cat(sample_part, '-->', result_part, '\n')
}

hist(population)
hist(statistics)

mn_sampling_distribution_mean <- mean(population)
sd_sampling_distribution_mean <- sd(population) / sqrt(sample_size)

mn<-min(statistics)
mx<-max(statistics)
x <- seq(mn,mx,1)
y<-dnorm(x, mean = mn_sampling_distribution_mean, sd = sd_sampling_distribution_mean)

hist(statistics, freq=FALSE)
points(x,y,type = "l")

