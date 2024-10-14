import numpy as np

def simulate_continuous_variable(n, mean=0, std=1):
    return np.random.normal(mean, std, n)

def simulate_discrete_variable(n, p=0.5):
    return np.random.binomial(1, p, n)