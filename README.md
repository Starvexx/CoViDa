# CoViDa
Corona Virus Data Analyzer

Version: 0.1

## Motivation
Due to the events of the Covid-19 pandemic outbreak, I have decided to create a small and simple tool
to visually depict casenumbers of the disease. I got the idea from [Worldometer](https://www.worldometers.info/coronavirus/)
when I found out that not all countries have graphical representations on the course of the outbreak.
However, the fine people that run Worldometer seem to update their webpage to provide graphs for all
countries over time. For instance this was the case for Austria and I started this project before they
provided provided graphs. Nevertheless I decided to keep working on it.

## What is this?
This is supposed to become a simple to use Python script that can plot the data on the Covid-19 outbreak.
It also fits the data to an exponential curve and to some extent tries to extrapolate the future development.
However, keep i mind that the model is a simple exponential development that does not take into account
any measures taken to contain the virus. It however should become visible if the measures taken are showing
effect.

## Dependencies
The Python packages used in the script are listed below.
- Numpy
- matplotlib
- scipy
- datetime
- argparse

If you are missing any of these packages the script will not run. To install them use Anaconda or pip.

### Windows
Open your Anaconda prompt and enter the following into your commandline:
```
conda install <package>
```
Where `<package>` is the name of the Phython package you want to install.

### Unix
Simply open a Terminal and enter the following:
```
pip install <package>
```
## Dataformat
So that the program can process the data, is has to be provided in a specific format. The script reads
as `.csv` file with seven columns. The first line in the file is as follows and defines the columns.
```
year, month, day, tested, infected, dead, recovered
```
Additionaly an example file is present in the repository. It holds the data for Austria since the
first case was officialy confirmed.

If you want to plot the data for your country, province or city, you will have to research the past
development of cases on your own and store them to a `.csv` file of the above described format.

## Usage
To run the script you first need to make it executable. On Unix machines simply `cd` to the folder
containing the script and execute the following command in a terminal.
```
chmod u+x corona.py
```
And to execute either copy the script to a folder that is part of your `$PATH` or or run from the
folder containing the script.
- If the script was copied to a `$PATH` folder enter the following into a terminal: `corona.py -f /path/to/file.csv`
- If you run from the folder the script is in enter this: `./corona.py -f /path/to/data.csv -t 30`

The `-t` option sets the number of days you want to plot the fitted functions. For instance, `-t 30`
will plot 30 days, starting from the first date listed in the datafile.
Also try the `-l` option for logaritmic plots.
