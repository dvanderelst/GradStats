## Set up parameters and initial conditions of model

S <- 10000
I <- 10
R <- 0
beta<- 0.025
gamma<- 1/250
N <- S + I + R

## Run model
S_trace <-c()
I_trace <-c()
R_trace <-c()

for(day in 1:1000)
{
  delta_S <- -(beta * I * S) / N
  delta_I <- ((beta * I * S))/N - gamma * I
  delta_R <- gamma * I
  
  S <- S + delta_S
  I <- I + delta_I
  R <- R + delta_R
  
  
  if(S < 0){S <- 0}
  if(I < 0){I <- 0}
  if(R < 0){R <- 0}
  
  S_trace <- c(S_trace, S)
  I_trace <- c(I_trace, I)
  R_trace <- c(R_trace, R)

  
  s<-paste(S,I,R)
  print(s)
  
}

plot(S_trace, type='l', col = 'red')
points(I_trace, type='l', col = 'green')
points(R_trace, type='l', col = 'blue')




