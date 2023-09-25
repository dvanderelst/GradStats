library(latex2exp)

par(mfrow=c(1,3))


# vary power
p_effect <- 0.5
alpha <- 0.05
t <- sprintf('$p_e$: %.2f, $\\alpha$ = %.2f', p_effect, alpha)
t <- TeX(t)
curve((p_effect * x) / (p_effect * (x - alpha) + alpha), from=0, to=1, xlab="Power (1 - beta)", ylab="PVV", main= t)


# vary alpha
p_effect <- 0.5
power <- 0.8
t <- sprintf('$p_e$: %.2f, power = %.2f', p_effect, power)
t <- TeX(t)
curve((p_effect * power) / (p_effect * (power - x) + x), from=0.001, to=0.1, xlab="Alpha", ylab= 'PVV', main= t)

# vary p_effect
power <- 0.8
alpha <- 0.05
t <- sprintf('$\\alpha$: %.2f, power = %.2f', alpha, power)
t <- TeX(t)
curve((x * power) / (x * (power - alpha) + alpha), from=0.001, to=1, xlab="p(effect)", ylab= 'PVV', main= t)


par(mfrow=c(1,1))
# vary p_effect
power <- 0.8
alpha <- 0.05
t <- sprintf('$\\alpha$: %.2f, power = %.2f', alpha, power)
t <- TeX(t)
curve((x * power) / (x * (power - alpha) + alpha), from=0.001, to=1, xlab="p(effect)", ylab= 'PVV', main= t)

