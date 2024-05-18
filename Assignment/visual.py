"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""


import matplotlib.pyplot as plt
from process import *
import csv


def display_pie(data):

    country_stats, country_list = data
    confirmed_cases = []
    for cc in country_stats:
        confirmed_cases.append(cc[0])
    fig, ax = plt.subplots()
    ax.pie(confirmed_cases,labels = country_list,autopct = '%.0f%%')
    ax.set_title('Confirmed Cases per Country/Region')
    ax.axis('equal')
    plt.show()

def bar_chart(data):
    country_stats, country_list = data
    confirmed_deaths = []
    for cc in country_stats:
        confirmed_deaths.append(cc[2])
    n = len(confirmed_deaths)
    #bubblesort descending oreder
    for i in range(n - 1,0,-1):
        for j in range(i):
            if confirmed_deaths[j] < confirmed_deaths[j + 1]:
                confirmed_deaths[j], confirmed_deaths[j + 1] = confirmed_deaths[j + 1], confirmed_deaths[j]
                country_list[j], country_list[j + 1] = country_list[j + 1], country_list[j]
    for i in range (len(confirmed_deaths)-1,4,-1):
        confirmed_deaths.pop(i)
        country_list.pop(i)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(country_list, confirmed_deaths)
    plt.show()