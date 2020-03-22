#! /usr/bin/env python3
"""
Author:     David Hernandez
E-Mail:     david.hernandez@univie.ac.at
Version:    0.1

This is a little script to analyze the Corona outbreak by passing a datafile
containing date, number of tests administered, number of infected, number of
deaths and number of cured/recovered persons.
    The script then will read the data and create plots so that it can be
analyzed visually.
"""
from matplotlib import pyplot as plt
from matplotlib import dates as mpldate
from scipy.optimize import curve_fit
import numpy as np
import datetime as dt
import argparse as ap

def func(x, a, b):
    """This is the function after which the data is fitted."""
    return a * np.exp(b * x)

if __name__ == "__main__":
    #==========================================================================#
    # Set up the argument parser.
    parser = ap.ArgumentParser(description="Plot some corona data.")
    parser.add_argument('--datafile', '-f',
                        type=str,
                        help='The datafile that contains the corona data.')
    parser.add_argument('--logaritmic', '-l',
                        action='store_true',
                        help='Plot the data on logarithmic scale.',
                        default=False)
    args = parser.parse_args()

    data = np.genfromtxt(args.datafile, delimiter=',', skip_header=1)

    days = []
    tested = []
    infected = []
    dead = []
    recovered = []

    for line in data:
        days.append(mpldate.date2num(dt.date(int(line[0]),
                                             int(line[1]),
                                             int(line[2]))))
        tested.append(line[3])
        infected.append(line[4])
        dead.append(line[5])
        recovered.append(line[6])

    days_new = np.arange(0, len(days), 1)
    popt, pcov = curve_fit(func, days_new, infected)

    timeline = np.arange(737480.0, 737480.0+30, 0.1)
    t_new = np.arange(0.0, 30.0, 0.1)
    fitted = []
    for t in t_new:
        fitted.append(func(t, *popt))

    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)

    ax1.plot_date(days, infected, label='Data')
    ax1.plot(timeline, fitted, label='Exponential fit')

    ax2.plot_date(days, dead, label='Dead')
    ax2.plot_date(days, recovered, label='Recovered')

    ax3.plot_date(days, tested)

    ax1.xaxis.set_tick_params(rotation=30, labelsize=10)
    ax1.grid(True)
    ax1.set_ylabel('Infected')
    ax2.xaxis.set_tick_params(rotation=30, labelsize=10)
    ax2.grid(True)
    ax2.set_ylabel('Persons')
    ax3.xaxis.set_tick_params(rotation=30, labelsize=10)
    ax3.grid(True)
    ax3.set_xlabel('Datum')
    ax3.set_ylabel('Persons')
    plt.show()
