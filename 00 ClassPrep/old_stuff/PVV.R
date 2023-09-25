alpha <-0.05
power <- 0.2

# if R is given but not p_effect: p_effect = R/(R+1)
prior_effect = 0.25

PVV <- (prior_effect * power) / (prior_effect * (power - alpha) + alpha)
print(PVV)
