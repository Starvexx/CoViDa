# CoViDa
Corona Virus Data Analyzer

Version: 0.1

## Motivation
Due to the events of the Covid-19 pandemic outbreak, I have decided to create a small and simple tool 
to visually depict casenumbers of the disease. I got the idea from [Worldometer](https://www.worldometers.info/coronavirus/)
when I found out that not all countries have graphical representations on the course of the outbreak.

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
