import numpy
import pandas
from matplotlib import pyplot
#dependent, independent: list [mean, variance]

import scipy.stats as stats

def getF(compare_data, dfn, dfd):
    maximum = numpy.max(compare_data)
    x_values = numpy.linspace(0, maximum, 1000)
    y_values =  stats.f.pdf(x_values, dfn, dfd)
    return x_values, y_values

def bivariate(dependent, independent, correlation, n):
    means = [dependent[0], independent[0]]
    cov = dependent[1] * independent[1] * correlation
    mean_mat = numpy.array(means)
    cov_mat = [[dependent[1] ** 2, cov], [cov, independent[1] ** 2]]
    cov_mat = numpy.array(cov_mat)
    data = numpy.random.multivariate_normal(mean_mat, cov_mat, n)
    data = pandas.DataFrame(data)
    data.columns = ['y', 'x']
    txt = f'y: {dependent}, x: {independent}, corr: {correlation}, n:{n}'
    return data, txt

def vlines(xs):
    ax = pyplot.gca()
    limit = ax.get_ylim()
    pyplot.vlines(xs, limit[0], limit[1])


def hlines(ys):
    ax = pyplot.gca()
    limit = ax.get_xlim()
    pyplot.hlines(ys, limit[0], limit[1])

