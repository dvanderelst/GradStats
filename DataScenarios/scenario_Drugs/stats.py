import numpy
import pandas
import statsmodels.formula.api as smf
from matplotlib import pyplot
from scipy.stats import ttest_ind, ttest_rel

def match_variables(data, variables):
    names = list(data.columns)
    if not isinstance(variables, (list, tuple)): variables = [variables]
    variables_lower = list2lower(variables)
    names_lower = list2lower(names)
    matched_variables = []
    failed_variables = []
    for lower, original in zip(variables_lower, variables):
        try:
            index = names_lower.index(lower)
            matched = names[index]
            matched_variables.append(matched)
        except:
            failed_variables.append(original)
    return matched_variables, failed_variables


def list2lower(lst):
    result = [x.lower() for x in lst]
    return result


def name_range(base, n):
    names = []
    for x in range(0, n): names.append(base + str(x))
    return names


def normalize(value, min_value, max_value):
    delta = max_value - min_value
    new = value - min_value
    new = new / delta
    if new < 0: new = 0
    if new > 1: new = 1
    return new



def group(data, groups, statistic='mean'):
    """
    Function simplifying grouping of data and calculating a statistic.

    :param data: Dataframe
    :param groups: List of variables names used to group the data
    :param statistic: A string indicating the statistic to calculate
    :return: The grouped data, as a dataframe
    """
    matched, failed = match_variables(data, groups)
    for x in failed: print('Warning: Can not find variable', x)
    grp = data.groupby(matched)
    table = eval("grp." + statistic + "()")
    table = table.reset_index()
    return table


def ttest(group1, group2, independent=True):
    if independent:
        result = ttest_ind(group1, group2)
        df = len(group1) + len(group2) - 2

    if not independent:
        result = ttest_rel(group1, group2)
        df = len(group1) - 1
    t = result[0]
    p = result[1]
    text = 't(%i) = %.2f, p = %.2f' % (df, t, p)
    return t, df, p, text


def regression(formula, data=None, typ=None):
    if typ == 'lin': model = smf.ols(formula=formula, data=data)
    if typ == 'log': model = smf.logit(formula=formula, data=data)
    fitted = model.fit()
    result = dict()
    result['fitted'] = fitted
    result['summary'] = fitted.summary2()
    result['prediction'] = pandas.DataFrame({'prediction': fitted.predict()})
    return result


def simple_regression(dependent, independent, data, typ='lin', do_plot=True):
    new_data = pandas.DataFrame()
    new_data['dependent'] = data[dependent]
    new_data['independent'] = data[independent]
    formula = 'dependent~independent'
    result = regression(formula, data=new_data, typ=typ)
    model = result['fitted']
    # Get prediction
    independent_data = new_data['independent']
    dependent_data = new_data['dependent']
    x_values = numpy.linspace(independent_data.min(), independent_data.max(), 100)
    x_values = pandas.DataFrame({'independent': x_values})
    prediction_data = model.predict(x_values)
    # Do plot
    if do_plot:
        pyplot.scatter(independent_data, dependent_data)
        pyplot.plot(x_values, prediction_data, 'r-')
        pyplot.xlabel(independent)
        pyplot.ylabel(dependent)
    result['X'] = x_values
    result['Y'] = dependent_data
    return result


def linear_regression(formula, data):
    result = regression(formula, data, typ='lin')
    return result


def logistic_regression(formula, data):
    result = regression(formula, data, typ='log')
    return result
