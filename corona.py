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
from matplotlib.dates import DateFormatter
from scipy.optimize import curve_fit
import numpy as np
import datetime as dt
import argparse as ap

def func(x, a, b):
    """This is the function after which the data is fitted."""
    return a * np.exp(b * x)

if __name__ == "__main__":
    # ======================================================================== #
    # Set up the argument parser.
    # -f, --datafile: This provides the path to the datafile.
    # -l, --logarithmic: This is a flag that triggers logaritmic plotting.
    parser = ap.ArgumentParser(description="Plot some corona data.")
    parser.add_argument('--datafile', '-f',
                        type=str,
                        help='The datafile that contains the corona data.')
    parser.add_argument('--runtime', '-t',
                        type=int,
                        help='Number of days to plot the fitted function.',
                        default=0)
    parser.add_argument('--logaritmic', '-l',
                        action='store_true',
                        help='Plot the data on logarithmic scale.',
                        default=False)
    args = parser.parse_args()

    # ======================================================================== #
    # Read the datafile and store the columns to lists.
    data = np.genfromtxt(args.datafile, delimiter=',', skip_header=1)

    # Extract the location name from the datafile name.
    country = args.datafile.split('_')[0]

    days = []           # The actual date
    tested = []         # The number of tested persons
    infected = []       # The number of infected persons
    dead = []           # The number of deceased persons
    recovered = []      # The number of recovered persons

    for line in data:
        days.append(mpldate.date2num(dt.date(int(line[0]),
                                             int(line[1]),
                                             int(line[2]))))
        tested.append(line[3])
        infected.append(line[4])
        dead.append(line[5])
        recovered.append(line[6])

    # ======================================================================== #
    # Fit the exponential function to the data.
    # days_new is the timeline staring at the first officialy confirmed case.
    # popt holds the optimized parameters for the curve fit.
    days_new = np.arange(0, len(days), 1)
    popt_i, pcov_i = curve_fit(func, days_new, infected)
    ### NaN handling TBD!!!
    # popt_t, pcov_t = curve_fit(func, days_new, tested[valid])

    # The actual timeline
    timeline = np.arange(days[0], days[0] + len(days) + args.runtime - 1, 0.1)
    # t_new is the number of days that shall be plotted using the parameters
    #   popt retrieved from the fit.
    t_new = np.arange(0.0, len(days) + args.runtime - 1, 0.1)
    # The datapoints for the extrapolated function, n. of infected
    fitted_i = []
    # The datapoints for the extrapolated function, nr. of tests
    fitted_t = []
    for t in t_new:
        fitted_i.append(func(t, *popt_i))
        # fitted_t.append(func(t, *popt_t))

    # ======================================================================== #
    # Plot the data.

    formatter = DateFormatter('%d.%m.%Y')

    fig = plt.figure(figsize=(8.27,11.69))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312, sharex=ax1)
    ax3 = fig.add_subplot(313, sharex=ax1)

    ax1.plot_date(days, infected, label='Infected')
    ax1.plot(timeline, fitted_i,
             label=f'Fit: f(x) = {popt_i[0]:.2f} * exp({popt_i[1]:.2f} * x)')

    ax2.plot_date(days, dead, label='Dead')
    ax2.plot_date(days, recovered, label='Recovered')

    ax3.plot_date(days, tested, label='Tests')
#    ax3.plot(timeline, fitted_t,
#             label=f'Fit: f(x) = {popt_t[0]:.2f} * exp({popt_t[1]:.2f} * x)')

    # ======================================================================== #
    # Formatting of the individual plots.
    ax1.xaxis.set_tick_params(rotation=30, labelsize=8)
    ax1.xaxis.set_major_formatter(formatter)
    ax1.legend(loc='upper left')
    ax1.grid(True)
    ax1.set_ylabel('Persons')
    if args.logaritmic:
        ax1.set_yscale('log')
        ax1.set_title('Infected (logarithmic scale)')
    else:
        ax1.set_title('Infected')

    ax2.xaxis.set_tick_params(rotation=30, labelsize=8)
    ax2.legend(loc='upper left')
    ax2.grid(True)
    ax2.set_ylabel('Persons')
    if args.logaritmic:
        ax2.set_yscale('log')
        ax2.set_title('Closed cases (logarithmic scale)')
    else:
        ax2.set_title('Closed cases')

    ax3.xaxis.set_tick_params(rotation=30, labelsize=8)
    ax3.legend(loc='upper left')
    ax3.grid(True)
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Persons')
    if args.logaritmic:
        ax3.set_yscale('log')
        ax3.set_title('Administered tests (logarithmic scale)')
    else:
        ax3.set_title('Administered tests')

    fig.suptitle(f'Corona data for {country}.')
    plt.subplots_adjust(top=0.92, bottom=0.1, left=0.11,
                        right=0.92, hspace=0.42, wspace=0.3)

    outfile = args.datafile.replace('_data.csv', '_plots.pdf')
    plt.savefig(outfile, format='pdf')
    plt.show()
