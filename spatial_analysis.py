# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oscar Johnson 10 April 2016

Copyright Oscar Johnson 2016
"""

import Mantel
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

'''
after running cluster analysis (AMOVA?)
iteratively compute all possible permutations of
comparisons between populations

partial mantel implementation within 'import Mantel'?
if not, could edit the code to allow for partial
'''
# np.linalg.lstsq(arrayA,arrayB)
# np.linalg.lstsq(dists1,dists2)

def sim():
    """
    simulate data
    length must be equal to redundant distance matrix
    """
    x = list(np.random.random(55))
    y = list(np.random.random(55))
    sim = Mantel.test(x, y)
    if args.1d == '1'
        
    return sim


def mant(x=dists1, y=dists2):
    """
    calculate a Mantel test with x and y
    """
    dists1 = [0.2, 0.4, 0.3, 0.6, 0.9, 0.4]
    dists2 = [0.3, 0.3, 0.2, 0.7, 0.8, 0.3]
    res = Mantel.test(dists1, dists2)
    return(res)


def p_mantel_1d(x, y, z):
    """
    takes three matrices; x, y, and z
    calculates the residuals of x and y
    and runs a Mantel test on the residuals vs z
    part of code comes from Mantel function
    """
    # Ensure that X and Y are formatted as Numpy arrays.
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    # Calculate the X and Y residuals
    x_residuals, y_residuals = x - x.mean(), y - y.mean()


def p_mantel_2d(x, y, z):
    """
    using 2 dimensional array
    """


def scat(x, y):
    """
    scatter plot of x and y
    """
    plt.scatter(x, y)
    plt.show()


def AMOVA():
    """
    run AMOVA test
    """


def main():
    mant()


if __name__ == '__main__':
    main()


if len(X.shape) == 2:
    X = spatial.distance.squareform(X, force='tovector', checks=False)
if len(Y.shape) == 2:
    Y = spatial.distance.squareform(Y, force='tovector', checks=False)
