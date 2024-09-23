import numpy
import library
import statsmodels.formula.api as smf
from matplotlib import pyplot

dependent = [0, 1.5]
independent = [0, 3]
correlation = 0.5
sample_size = 30

# %%
fvalues = []

for i in range(10000):
    if i % 1000 == 0: print(i)
    null_hypothesis_data, description = library.bivariate(dependent, independent, 0, sample_size)
    null_model = smf.ols('y ~ x', data=null_hypothesis_data)
    result = null_model.fit()
    fvalue = result.fvalue
    fvalues.append(fvalue)
# %%
sampled_data, description_sampled = library.bivariate(dependent, independent, correlation, sample_size)
model = smf.ols('y ~ x', data=null_hypothesis_data)
result = null_model.fit()
sampled_fvalue = result.fvalue

#%%
dfmodel = result.df_model
dfresidual = result.df_resid
x_f, y_f = library.getF(fvalues, dfmodel, dfresidual)
sampled_p = numpy.mean(fvalues > sampled_fvalue)

pyplot.figure()
pyplot.hist(fvalues, density=True, bins=250)
pyplot.plot(x_f, y_f)
library.vlines(sampled_fvalue)

pyplot.xlim(0, 5)

pyplot.xlabel('F value')
pyplot.ylabel('Density')
pyplot.legend(['Simulated f-values', 'F sampled', 'Theoretical distribution'])
pyplot.title('Simulated distribution:\n' + description)
pyplot.text(2, 1, s='Sampled Data:\n' + description_sampled)

pyplot.axvspan(sampled_fvalue, numpy.max(fvalues), color='red', alpha=0.25)
pyplot.text(2, 1.5, s='Sampled p value: ' + str(sampled_p))


pyplot.show()
