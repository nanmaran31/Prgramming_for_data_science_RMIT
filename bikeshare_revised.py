import time
import pandas as pd
import datetime as dt
from datetime import timedelta

"""
These are the dictionaries that will be used throughout the code

"""

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_list = ['chicago', 'new york', 'washington']
month_list = ['January', 'February', 'March', 'April', 'May', 'June']
day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
type_list = ['month','day','none', 'both']


def get_filters():
    """
    Code to get the filters for data computation from user input. Users are first asked to filter the city.
    They are then given options to filer the data further - by a particular month/day/both or none. If they choose none
    the data is filtered just by the city.

    """
    print('Hello! Let\'s explore some US bikeshare data!')
    res='yes'

    while res=='yes':
        city=input("Would you like to look at the data for Chicago, New York, or Washington? \n")
        city=city.lower()

        if city in city_list: break
        else:
            print(f'Enter a valid city {city_list}')
            city=input()
            res='no'
    print("Entered city is   ",city)

    res='yes'
    while res=='yes':
        get_filter=input("Would you like to filter the data by month, day, both or none at all(please enter none) \n")
        get_filter=get_filter.lower()

        if get_filter in type_list: break
        else:
            print(f'Enter a valid response {type_list}')
            get_filter=input()
            print("Your option is   ",get_filter)
            break


    if (get_filter == 'month'):
                day = 'all'

                res='yes'

                while res=='yes':
                    month=input(f'Enter name of a month {month_list}\n')
                    month=month.title()
                    if month in month_list: break
                    else:
                        print(f'Enter a valid Month {month_list}')
                        month=input()
                        print("Month Entered is   ",month)
                        res='no'

    elif (get_filter == 'day'):
                month = 'all'

                while res=='yes':
                    day=input(f'Enter a day {day_list}\n')
                    day=day.title()
                    if day in day_list: break
                    else:
                        print(f'Enter a valid day {day_list}')
                        day=input()
                        print("Day is   ",day)
                        res='no'

    elif (get_filter == 'both'):

       res='yes'

       while res=='yes':
                    month=input(f'Enter name of a month {month_list}\n')
                    month=month.title()
                    if month in month_list: break
                    else:
                        print(f'Enter a valid Month {month_list}')
                        month=input()
                        print("Month Entered is   ",month)
                        res='no'


       while res=='yes':
            day=input(f'Enter a day {day_list}\n')
            day=day.title()
            if day in day_list: break
            else:
                        print(f'Enter a valid day {day_list}')
                        day=input()
                        print("Day is   ",day)
                        res='no'


    else :
        day = 'all'
        month = 'all'



    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if month != 'all':

        df = df[df['month'] == month]


    if day != 'all':

        df = df[df['day_of_week'] == day]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    count_pop_month = df['month'].value_counts()[popular_month]

    print('Most Popular Month is :', popular_month)
    print('Count:', count_pop_month)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    count_pop_day =df['day_of_week'].value_counts([popular_day_of_week])

    print('Most common day is :', popular_day_of_week)
    print('Count:', count_pop_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    count_pop_hour = df['hour'].value_counts()[popular_hour]

    print('Most common Start Hour:', popular_hour)
    print('Count:', count_pop_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mode_start_station = df['Start Station'].mode()[0]
    print('The most common start station is', mode_start_station)

    count_start_station = df['Start Station'].value_counts()[mode_start_station]
    print('Count:',count_start_station)

    # display most commonly used end station
    mode_end_station = df['End Station'].mode()[0]
    print('The most common end station is', mode_end_station)

    count_end_station= df['Start Station'].value_counts()[mode_end_station]
    print('Count:',count_end_station)
    # display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most popular trip is',popular_trip)

    count_popular_trip= (df['Start Station'] + ' to ' + df['End Station']).value_counts()[popular_trip]
    print('Count:',count_popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
        # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    sec = total_travel_time
    res = sec/(3600)
    print('The total trip duration is:',res,' hours')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    sec1 = mean_travel_time
    res1 = sec1/(3600)
    print('Average duration of a trip is:',res1,' hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Here are the stats for the different types of users:\n', user_type_count)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print('\nThe oldest users were born in:', earliest_year)

        recent_year = df['Birth Year'].max()
        print('\nThe youngest users were born in:', recent_year)


        common_year = df['Birth Year'].mode()[0]
        print('\nThe most common year of birth among the users is:', common_year)

        count_common_year= df['Birth Year'].value_counts()[common_year]
        print('Count:',count_common_year)

    if 'Gender' in df:
        gender_stats = df['Gender'].value_counts()
        print('\nHere is the gender breakdown of users:\n',gender_stats)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_raw_data(df):
    """
    Asks user if they want to view the first 5 lines of filtered raw data. If they select yes, then it asks if they want
    to view the next 5 and so on until they say no.
    """
    print ('Would you like to see the first 5 lines of raw data?')
    raw_data = input('yes/no\n')
    raw_data=raw_data.lower()

    if (raw_data == 'yes'):
        x=5
        print(df[:x])

        next_iteration = input('\n Would you like to view the next 5 lines? yes/no\n')
        next_iteration=next_iteration.lower()

        while next_iteration == 'yes':
            print(df[x:(x+5)])
            next_iteration = input('\n Would you like to view the next 5 lines? yes/no\n')
            next_iteration=next_iteration.lower()

        else:
            return


    else:
        return

def main():
    """
    Calling all the functions
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_raw_data(df)

        """
        Giving the users an option to restart the entire program to look at other data.
        """
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        restart = restart.lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
