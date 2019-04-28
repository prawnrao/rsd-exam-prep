# QUESTION 1
############

# (a)

import numpy as np
import json
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


def gen_json(csvdata):
    dic = {}
    for entry in csvdata:
        k = int(entry[0])
        v = entry[2]

        if k in dic:
            dic[k].append(v)
        else:
            dic[k] = [v]

    with open('data.json', 'w') as outfile:
        json.dump(dic, outfile, indent=4)


# (b)

def plot_daily_rainfall(json_file, year, color='b'):
    with open(json_file, 'r') as infile:
        data = json.load(infile)

    yearly_rainfall = data[year]
    yearly_rainfall = np.array(yearly_rainfall)
    days = np.arange(1, len(yearly_rainfall) + 1, 1)
    plt.plot(days, yearly_rainfall, color)
    plt.xlabel('Days')
    plt.ylabel('Rainfall (mm)')
    plt.savefig('{}.png'.format(year))
    plt.clf()


# (c)

def plot_means(json_file, year1, year2, color='b'):
    means = []
    with open(json_file, 'r') as infile:
        data = json.load(infile)
    curr_year = int(year1)

    while curr_year <= int(year2):
        curr_data = data[str(curr_year)]
        means.append(np.mean(curr_data))
        curr_year += 1

    means = np.array(means)
    years = np.arange(int(year1), int(year2) + 1, 1)
    plt.plot(years, means)
    plt.xlabel('Years')
    plt.ylabel('Annual average rainfall (mm)')
    plt.savefig('means.png')
    plt.clf()


# (d)

def correct_value(value):
    return value * (1.2**np.sqrt(2.0))


def correct_annual_values_1(annual_rainfall):
    """ For loop method
        Pros: more readable
        Cons: less compact
    """
    corrected_rainfall = []
    for daily_rainfall in annual_rainfall:
        corrected_rainfall.append(correct_value(daily_rainfall))

    return corrected_rainfall


def correct_annual_values_2(annual_rainfall):
    """ List comprehension method
        Pros: more compact
        Cons: less readable
    """
    return [correct_value(value) for value in annual_rainfall]


if __name__ == '__main__':
    csvdata = \
        np.genfromtxt('/Users/Pranav/Downloads/MPHYG001-2018/MPHYG001_files/python_language_1/python_language_1_data.csv',
                      names=True, delimiter=',')
    gen_json(csvdata)
    plot_daily_rainfall('data.json', '1998')
    plot_means('data.json', '1988', '2000')
    