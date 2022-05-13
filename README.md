# Explore US Bikeshare Data

![Explore US Bikeshare Data](https://video.udacity-data.com/topher/2018/March/5aa7718d_divvy/divvy.jpg "Explore US Bikeshare Data")

---

## Project Overview

---

In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

---

### Project Needs

---
the main idea of this project to use python to get some descriptive statistics for specific dataset using both Python and Pandas.

Your program will take user input for the city (e.g. Chicago), month for which the user wants to view data (e.g. January; also includes an 'all' option), and day for which the user wants to view data (e.g. Monday; also includes an 'all' option).

Upon receiving the user input, it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not. Following the input received, the program prints the following details:

Most popular month
Most popular day
Most popular hour
Most popular start station
Most popular end station
Most popular combination of start and end stations
Total trip duration
Average trip duration
Types of users by number
Types of users by gender (if available)
The oldest user (if available)
The youngest user (if available)
The most common birth year amongst users (if available)

---

### Python

[Python](https://www.python.org/ "Python")

* Using Python to get some inputs **Right Inputs** from user to use it in description of the data
* Also will use it to create some functions to give more functionality to the project and link its parts togethers  

### Pandas

[Pandas](https://pandas.pydata.org/ "Pandas")

you will use it to manipulate the data to get its insides information.

### Time

[Time](https://docs.python.org/2/library/time.html "Time")

you will use this package to calculate some data using it

#### Important Note

If you will use the data on your own PC don't forget to install Pandas
``` bash
pip install pandas
```

## Things to remembers

If you process this as Udacity project you will be needing to complete some functions according to the instructor to do instructions

Example

```py

def get_filters():

 """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)
```
---
### Project Data

you will use the following 3 files for this project 

1. chicago.csv
1. new_york_city.csv
1. washington.csv
