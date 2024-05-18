"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""




import csv

from Assignment.tui import serial_number, observation_dates



def totalnumber(data):
     return len(data)


def retrieve_record(data):
    s_n = serial_number()
    for record in data:
        if int(record[0]) == s_n:
            return record


def retrieve_observ_dates(data):
    record_dates=[]
    dates = observation_dates()
    for record in data:
        if record[1] in dates:
            record_dates.append(record)
    return record_dates


def grouped_info(data,country):
    record_country = []
    for record in data:
        if record[3] == country:
            record_country.append(record)
    return record_country

def summary(data):
    country_list = []
    country_stats = []
    for record in data:
        if not record[3] in country_list:
            country_list.append(record[3])
            country_stats.append([0,0,0])
    for record in data:
        for i in range (len(country_list)):
            if record[3] == country_list[i]:
                country_stats[i][0] += int(record[5])
                country_stats[i][1] += int(record[6])
                country_stats[i][2] += int(record[7])
    return country_stats, country_list

def summary_print(data):
    i = 0
    #data[0] = country stats
    #data[1] = country list
    #a better print
    for c in data[1]:
        print(c,": ",end="")
        print(data[0][i][0])
        print("  "," " * len (c),end="")
        print(data[0][i][1])
        print("  "," " * len (c),end="")
        print(data[0][i][2])
        i += 1