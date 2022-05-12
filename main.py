import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

Month_DATA = ["january", "february", "march", "april", "may", "june", "all"]

Day_DATA = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
choosen_responce = ["yes", "no"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please input one of the following city Chicago, New York city, Washington -> \n").lower()
    while city not in CITY_DATA:
        city = input(
            "Please input valied city from the following cities Chicago, New York city, Washington -> \n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(
        "Please input one of the following monthes January, February, March, April, May, June Or All for all monthes -> \n").lower()
    while month not in Month_DATA:
        month = input(
            "Please input valied month of the following monthes January, February, March, April, May, June Or All for all monthes -> \n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        "Please input a day of the week you want to filter\nby Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all for All week days -> \n").lower()
    while day not in Day_DATA:
        day = input(
            "Please input valied day of the week you want to filter by Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All for all week days -> \n").lower()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load all datasets as one dataframe

    df = pd.read_csv(CITY_DATA[city])

    # Checking dataframe info
    # print(df.info())

    # convert the Start Time column from string to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # convert the End Time column from string to datetime
    df["End Time"] = pd.to_datetime(df["End Time"])
    # Testing my changes
    # print(df.info())
    # create new column called month from Start Time column
    df["Month"] = df["Start Time"].dt.month
    # Testing my changes
    # print(df.info())
    # print(df["Month"])
    # create new column called "DOW" - Days of the week- from  Start Time column
    df["DOW"] = df["Start Time"].dt.weekday_name
    # Testing my changes
    # print(df["DOW"].head())
    # create new column called "hour" - from  Start Time column
    df["hour"] = df["Start Time"].dt.hour
    # Month filltering process

    if month != "all":
        month = Month_DATA.index(month) + 1
        # created filtered datafram by month
        df = df[df["Month"] == month]
    # testing my code
    # print(df.head())
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["DOW"] == day.title()]

    # print(df.info())
    df = df.drop("Unnamed: 0", axis=1)
    # print(df.info())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    start_time = time.time()
    print("Calculating The Most Common Month & Days and Hours...")

    # TO DO: display the most common month
    most_common_month = df["Month"].mode()[0]
    month_name = Month_DATA[most_common_month - 1]
    print("The most Common Month: " + month_name.title())

    # TO DO: display the most common day of week
    most_common_day = df["DOW"].mode()[0]
    print("The most Common day:", most_common_day)

    # TO DO: display the most common start hour

    common_hour = df["hour"].mode()[0]
    print("The most Common Hour: " + str(common_hour) + ":00")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most Commonly used start station is: ", common_start_station.title())

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("The most Commonly used end station is: ", common_end_station.title())

    # TO DO: display most frequent combination of start station and end station trip
    Combination_station = df.groupby(['Start Station', 'End Station']).count()

    print('The most Commonly used combination of start station and end station trip is:\n',
          Combination_station.idxmax()[0][0],
          " _ ", Combination_station.idxmax()[0][1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
              df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('The total travel time in hours is roughly', round(total_travel_time / 60 / 60, 1), "Hours")
    print('The total travel time in days is roughly', round(total_travel_time / 60 / 60 / 24, 1), "Days")

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is:", round(mean_travel_time / 60, 1), "Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    """Args:
       df - Pandas DataFrame containing city data filtered by month and day"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The user Types are:\n", user_types)
    # TO DO: Display counts of gender
    try:
        gender_types = df["Gender"].value_counts()
        print("The gender Types are:\n", gender_types)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df["Birth Year"].min()
        print("\nThe earliest birth year is :", int(earliest_year))
    except KeyError:
        print("\nThe earliest birth year:\nNo data available for this month.")

    try:
        recent_year = df["Birth Year"].max()
        print("\nThe recent birth year is:", int(recent_year))
    except KeyError:
        print("\nThe recent birth year:\nNo data available for this month.")

    try:
        common_year = df["Birth Year"].value_counts().idxmax()
        print("\nThe commen birth year is:", int(common_year))
    except KeyError:
        print("\nThe commen birth year is:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """This function show the user some date after selecting the city the month
    and the day
    Args:
         df - Pandas DataFrame containing city data filtered by month and day"""
    data_index = 0
    displaly_data_answer = input("would you like to see some data ->\n").lower()
    while displaly_data_answer not in choosen_responce:
        print("invalied answer only yes or no accepted ->")
        displaly_data_answer = input("would you like to see some data ->\n").lower()
    while displaly_data_answer in choosen_responce:
        if displaly_data_answer == "no":
            return
        elif displaly_data_answer == "yes":

            print(df[data_index:data_index + 5])
            data_index += 5
            displaly_data_answer = input("would you like to see more data->\n").lower()
            if displaly_data_answer not in choosen_responce:
                print("invalied answer only yes or no accepted ->")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()