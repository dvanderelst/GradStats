import Utils
import numpy as np
import statsmodels.api as sm
import scipy.stats as stats
from matplotlib import pyplot as plt

# This script simulates sampling repeatedly from a population.
# It fits two models to the data: a simple model with one predictor and a full model with three predictors.
# It then compares the two models using ANOVA.
# The F-values are calculated automatically and manually.
# The F-values are then compared using histograms.

# The script also plots the F-distribution, **assuming that the null hypothesis is true**.
# This is the distribution that the F-values should follow if the null hypothesis is true.

# You can demonstrate that the F-distribution is correct by changing the coefficients of the B and C predictors to zero.
# In this case, the null hypothesis **is true**, and the F-values should follow the F-distribution.
# If the coefficients of B or C are not zero, the null hypothesis is false, and the F-values should not follow the F-distribution.
# In fact, then the F-values should be higher than the F-distribution predicts.

n = 100
coefficient_A = 0.01
coefficient_B = 0.0
coefficient_C = 0.025

automatic_f_values = []
manual_f_values = []
p_values = []

for i in range(5000):

    variable_A = Utils.simulate_continuous_variable(100)
    variable_B = Utils.simulate_continuous_variable(100)
    variable_C = Utils.simulate_continuous_variable(100)
    error = Utils.simulate_continuous_variable(100, std=0.1)

    dependent = variable_A * coefficient_A + variable_B * coefficient_B + coefficient_C * variable_C + error

    # Run partial linear regression (simple model with A)
    X_simple = np.column_stack((variable_A,))
    X_simple = sm.add_constant(X_simple)
    simple_model = sm.OLS(dependent, X_simple)
    results_simple_model = simple_model.fit()
    error_simple_model = results_simple_model.resid

    # Run full linear regression (full model with A, B, and C)
    X_full = np.column_stack((variable_A, variable_B, variable_C))
    X_full = sm.add_constant(X_full)
    full_model = sm.OLS(dependent, X_full)
    results_full_model = full_model.fit()
    error_full_model = results_full_model.resid

    # Compare the two models using ANOVA
    f_test = sm.stats.anova_lm(results_simple_model, results_full_model)
    automatic_f_value = f_test['F'][1]
    p_value = f_test['Pr(>F)'][1]

    # Get dof for the models
    dof_simple = float(results_simple_model.df_resid)
    dof_full = float(results_full_model.df_resid)

    # Correct delta_dof based on the number of predictors added (2 in this case)
    delta_dof = dof_simple - dof_full

    # Calculate the F-statistic manually
    error_simple_model = np.sum(error_simple_model ** 2)
    error_full_model = np.sum(error_full_model ** 2)
    manual_f_value = ((error_simple_model - error_full_model) / delta_dof) / (error_full_model / dof_full)
    automatic_f_values.append(automatic_f_value)
    manual_f_values.append(manual_f_value)
    p_values.append(p_value)

    if i%100 == 0:
        print('Iteration: ', i)
        print('Automatic F-value: ', automatic_f_value)
        print('Manual F-value: ', manual_f_value)
        print('')

# %%

# Get the x values for the F-distribution
# This is the F distribution, assuming that the null hypothesis is true
# In other words, it assumes that the full model is not better than the simple model
x = np.linspace(0, max(automatic_f_values), 1000)
y = stats.f.pdf(x, 2, dof_full)

# Plot histograms of automatic and manual F-values
plt.figure(figsize=(5, 6))
plt.subplot(2,1,1)
plt.hist(automatic_f_values, bins=50, alpha=0.5, density=True, label='Automatic F-values')
plt.hist(manual_f_values, bins=50, alpha=0.5, histtype='step', density=True, label='Manual F-values')
plt.plot(x, y, label='F-distribution (model 2 is not better than model 1)')
plt.xlim(0, max(automatic_f_values))
plt.title('F-values')
plt.xlabel('F-value')
plt.ylabel('Density')
plt.legend()
plt.subplot(2,1,2)
plt.hist(p_values, bins=50, alpha=0.5, density=True, label='P-values')
plt.title('P-values')
plt.xlabel('P-value')
plt.ylabel('Density')
plt.tight_layout()
plt.show()
