# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oscar Johnson 15 April 2016

Copyright Oscar Johnson 2016

after running a cluster analysis (AMOVA?)
iteratively compute all possible permutations of
comparisons between populations

partial mantel implementation within 'import Mantel'?
if not, could edit the code to allow for partial
"""


import os
import pdb
import glob
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

import Mantel


def get_args():
    parser = argparse.ArgumentParser(
            description="""mantel test and partial mantel test""")
    parser.add_argument('--in_dir',
                        type=str,
                        required=True,
                        help="directory containing 3 csv files",
                        )
    return parser.parse_args()


def sim():
    """
    simulate data and run Mantel
    length must be equal to redundant distance matrix
    """
    x_condensed = np.array(list(np.random.random(91)))
    y_condensed = np.array(list(np.random.random(91)))
    sim = Mantel.test(x_condensed, y_condensed)
    # if args.1d == '1'
    return sim


def sim_full():
    x_full = np.array(list(np.random.random(100)))
    y_full = np.array(list(np.random.random(100)))
    r1 = x_full.reshape(10, 10)
    r2 = y_full.reshape(10, 10)


def matrix_man(x1, y1):
    """manipulate full data matrix to work with Mantel.test"""
    xlist = []
    ylist = []
    for v in x1:
        xlist.extend(list(v))
    for v in y1:
        ylist.extend(list(v))
    # pdb.set_trace()
    while 0.0 in xlist:
        xlist.remove(0.0)
    while 0.0 in ylist:
        ylist.remove(0.0)
    return(xlist, ylist)


def mant(x=[0.2, 0.4, 0.3, 0.6, 0.9, 0.4],
         y=[0.3, 0.3, 0.2, 0.7, 0.8, 0.3]):
    """
    calculate a Mantel test with x and y
    has default of sample data from jwcarr
    converts to condensed matrix if needed
    """
    if x[0][1] == 0:
        x, y = matrix_man(x, y)
    else:
        pass
    res = Mantel.test(x, y)
    return(res)


def p_mantel(x, y, z):
    """
    takes three 2-dimensional matrices; x, y, and z
    calculates the linear regression of x and z, and y and z
    and runs a Mantel test on these matrices
    using 2 dimensional arrays
    """
    reg1, a1, b1, c1 = np.linalg.lstsq(x, z) # linear regression
    reg2, a2, b2, c2 = np.linalg.lstsq(y, z) # linear regression
    r1, r2 = matrix_man(reg1, reg2)
    res = Mantel.test(r1, r2)
    return(res)


def scat(x, y):
    """
    scatter plot of x and y
    need to edit this to include the linear regression from Mantel
    """
    plt.scatter(x, y)
    plt.show()


def AMOVA():
    """
    run AMOVA test
    """


def main():
    args = argparse.get_args()
    os.chdir(os.path.abspath(args.in_dir))
    x1 = np.array([[0.2, 0, 0],
                [0.4, 0.3, 0],
                [0.6, 0.9, 0.4]])
    y1 = np.array([[0.3, 0, 0],
                [0.3, 0.2, 0],
                [0.7, 0.8, 0.3]])
    z1 = np.array([[1, 0, 0],
                [1, 1, 0],
                [0, 0, 0]])
    # mant()
    f_man = mant(x1, y1)
    p_man = p_mantel(x1, y1, z1)
    print('r2 of full mantel: {} \nr2 of partial mantel: {}'.format(f_man[0],
          p_man[0]))

if __name__ == '__main__':
    main()
