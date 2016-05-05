# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oscar Johnson 15 April 2016

Copyright Oscar Johnson 2016

input directory must contain three .csv files:
genetic distance must have the  file name starting with 'gen'
geographic distance must have the  file name starting with 'geo'
control (for partial mantel) must have the file name starting with 'control'


ideas:
after running a cluster analysis (AMOVA?)
iteratively compute all possible permutations of
comparisons between populations
"""


import os
import sys
import shlex
import subprocess
# import csv
# import pdb
import glob
import argparse
import numpy as np
from pandas import read_csv
from scipy import cluster
import matplotlib.pyplot as plt
# from scipy.stats import linregress

import Mantel


def get_args():
    parser = argparse.ArgumentParser(
            description="""mantel test and partial mantel test""")
    parser.add_argument('--in_dir',
                        type=str,
                        required=True,
                        help="directory containing 2 or 3 csv files",
                        )
    parser.add_argument('--out_dir',
                        type=str,
                        required=True,
                        help="full directory for output",
                        )
    parser.add_argument('--sim',
                        type=str,
                        required=True,
                        help="enter 'y' to simulate data, 'n' to skip",
                        )
    parser.add_argument('--m',
                        type=str,
                        required=True,
                        help="'f' for full, 'p' for partial, 'n' to skip",
                        )
    return parser.parse_args()


def mant(x=[0.2, 0.4, 0.3, 0.6, 0.9, 0.4],
         y=[0.3, 0.3, 0.2, 0.7, 0.8, 0.3]):
    """
    calculate a Mantel test with x and y
    has default of sample data from jwcarr
    converts to condensed matrix if needed
    """
    if x[0][1] == 0:  # checks if matrix is condensed
        x, y = matrix_man(x, y)
    else:
        pass
    result = Mantel.test(x, y)
    return(result)


def p_mantel(x, y, z):
    """
    takes three 2-dimensional matrices; x, y, and z
    calculates the linear regression of x and z, and y and z
    and runs a Mantel test on these new matrices of residuals
    using 2 dimensional arrays
    """
    reg1, a1, b1, c1 = np.linalg.lstsq(x, z)  # linear regression
    reg2, a2, b2, c2 = np.linalg.lstsq(y, z)  # linear regression
    r1, r2 = matrix_man(reg1, reg2)
    result = Mantel.test(r1, r2)
    return(result)


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


def matrix_man_2(x1):
    """
    manipulate full data matrix to work with Mantel.test
    this function can take a single data matrix instead of two
    also works with residual matrices where the off-values aren't exactly zero
    """
    xlist = []
    for v in x1:
        xlist.extend(list(v))
    # pdb.set_trace()
    for val in xlist:
        if val < 0.000001:
            xlist.remove(val)
    #while 0.0 in xlist:
    #    xlist.remove(0.0)
    return(xlist)


def AMOVA(x, y):
    """
    run AMOVA test through arlecore
    this is not working
    """
    command = 'arlecore -args {}'.format(x, y)
    cmd = shlex.split(command)
    process = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True)
    return(process)


def cluster_data(gen_file):
    """
    clusters input data and decides whether
    to re-run each cluster in Mantel
    only works with full Manel test
    """    
    res = cluster.hierarchy.fclusterdata(np.array(gen_file), 2)
    return(res)


def sim():
    """
    REDUNDANT FUNCTION, need to edit
    simulate data and run Mantel with 1 dimensional data
    length must be equal to redundant distance matrix
    """
    x_condensed = np.array(list(np.random.random(91)))
    y_condensed = np.array(list(np.random.random(91)))
    sim = Mantel.test(x_condensed, y_condensed)
    # if args.1d == '1'
    return sim


def convert(arr):
    """takes array and adds zeros above diagonal"""
    counter = 1
    for row in arr:
        row[counter:] = 0
        counter += 1
    return(arr)


def sim_full():
    """
    simulates data and runs Mantel with 2 dimensional data
    for one population
    """
    x_full = np.array(list(np.random.random(100)))
    y_full = np.array(list(np.random.random(100)))
    r1 = x_full.reshape(10, 10)
    r2 = y_full.reshape(10, 10)

    # make matrices non-redundant
    r1 = convert(r1)
    r2 = convert(r2)

    m1, m2 = matrix_man(r1, r2)
    res = Mantel.test(m1, m2)
    return(res, m1, m2)


def run_sim():
    """
    if user wants to simulate data, this will run and print the results
    """
    # these are default example data
    x1 = np.array([[0.2, 0, 0],
                   [0.4, 0.3, 0],
                   [0.6, 0.9, 0.4]])
    y1 = np.array([[0.3, 0, 0],
                   [0.3, 0.2, 0],
                   [0.7, 0.8, 0.3]])
    z1 = np.array([[1, 0, 0],
                   [1, 1, 0],
                   [0, 0, 0]])

    f_man = mant(x1, y1)
    p_man = p_mantel(x1, y1, z1)
    print('\nresults using default example data')
    print('r2 of full mantel: {}'.format(f_man[0]))
    print('p-value of full mantel: {}'.format(f_man[1]))
    print('z-score of full mantel: {}'.format(f_man[2]))
    print('\nr2 of partial mantel: {}'.format(p_man[0]))
    print('p-value of partial mantel: {}'.format(p_man[1]))
    print('z-score of partial mantel: {}'.format(p_man[2]))

    # plots default sample data
    # p1, p2 = matrix_man(x1, y1)
    # plot_regression(p1, p2, 1)

    sim = sim_full()
    print('\n\nresults using simulated data from 1 population')
    print('r2 of full mantel: {}'.format(sim[0][0]))
    print('p-value of full mantel: {}'.format(sim[0][1]))
    print('z-score of full mantel: {}'.format(sim[0][2]))
    print('\n')

    # plots simulated data of one population
    plot_regression(sim[1], sim[2], 1)


def plot_regression(x, y, d):
    """
    plot regression of two matrices x and y
    and degrees of freedom (d)
    from http://stackoverflow.com/questions/7941226/
    this is not entirely accurate because standard matrix regression
    is not the same as a Mantel correlation, but it's the best I can do
    """
    # Find the slope and intercept of the best fit line
    slope, intercept = np.polyfit(x, y, d)

    # Create a list of values in the best fit line
    ablineValues = []
    for i in x:
        ablineValues.append(slope * i + intercept)

    # Plot the best fit line over the actual values
    plt.plot(x, y, '.')
    plt.plot(x, ablineValues, 'b')
    plt.title('slope: {}'.format(slope))
    plt.show()


def writer(args, data):
    """takes mantel results and writes to file"""
    os.chdir(os.path.abspath(args.out_dir))
    # np.savetxt("result.csv", array, delimiter=",")
    with open("results.txt", 'w') as out_file:
        out_file.write('verdical correlation {}'.format(str(data[0])))
        out_file.write('\np-value {}'.format(str(data[1])))
        out_file.write('\nz-score {}'.format(str(data[2])))


def main():
    args = get_args()
    # os.chdir(os.path.abspath(args.in_dir))

    # get file paths
    f1 = glob.glob(args.in_dir + 'geo*.csv')
    f2 = glob.glob(args.in_dir + 'gen*.csv')
    f3 = glob.glob(args.in_dir + 'control*.csv')
    # pdb.set_trace()

    # import files to numpy
    geo_file = np.array(read_csv(f1[0], header=None))
    gen_file = np.array(read_csv(f2[0], header=None))
    if len(f3) != 0:
        control_file = np.array(read_csv(f3[0], header=None))
    # pdb.set_trace()
    
    # run clustering algorithm
    check = cluster_data(gen_file)
    if len(set(check)) > 1:
        print('your population clusters are: {}'.format(check))
        sys.exit("your data are clustering into more than one population")
    elif len(set(check)) == 1:
        print('your data are clustering into one population, all is well')

    # do stuff with files
    if args.m.lower() == 'f':
        m = mant(geo_file, gen_file)
        print('verdical correlation of full mantel: {}'.format(m[0]))
        print('p-value of full mantel: {}'.format(m[1]))
        print('z-score of full mantel: {}'.format(m[2]))
        writer(args, m)
        geo, gen = matrix_man(geo_file, gen_file)
        plot_regression(geo, gen, 1)
    elif args.m.lower() == 'p':
        p = p_mantel(geo_file, gen_file, control_file)
        print('r2 of partial mantel: {}'.format(p[0]))
        print('p-value of partial mantel: {}'.format(p[1]))
        print('z-score of partial mantel: {}'.format(p[2]))
        writer(args, p)
    elif args.m.lower() == 'n':
        pass

    if args.sim.lower() == 'y':
        run_sim()
    elif args.sim.lower() == 'n':
        pass

    # if user didn't input any commands
    low = args.m.lower()
    if args.sim.lower() != 'y' and low != 'f' and low != 'p':
        print('you have not entered any useful commands, please try again!')

if __name__ == '__main__':
    main()
