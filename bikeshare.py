#First change
#Second change

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Please select the city: ')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('PlEAse seLECt from chicAgO, new yOrk CITY, washington: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please select the month: ')
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('PlEAse seLECt from all, JANUarY, february, ... , JUNE: ').lower()
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('PlEAse seLECt the day: ').lower()

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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time and End Time columns into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of week from Start Time into new columns 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: ', df['month'].value_counts().idxmax())


    # TO DO: display the most common day of week
    print('The most common day is: ', df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common hour is: ', df['hour'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: ', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('The most commonly used end station is: ', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is: ', df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time (hours) is: ", df['Trip Duration'].sum() / 3600.0)

    # TO DO: display mean travel time
    print("Mean travel time (hours) is: ", df['Trip Duration'].mean() / 3600.0)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: ', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in YOUR_DATAFRAME:
        gender_count = df['Gender'].value_counts()
    # Only access Gender column in this case 
        print('Counts of user gender: ', gender_count)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = int(df['Birth Year'].min())
    most_recent_year = int(df['Birth Year'].max())
    most_common_year = int(df['Birth Year'].value_counts().idxmax())
    print('The earliest year of birth is: ', earliest_year, 
          '. The most recent year of birth is: ', most_recent_year,     
          '. The most common year of birth is: ', most_common_year)
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def raw_data (df):
#Displays the data due filteration. 5 rows will added in each press

    print('press enter to see row data, press no to skip')
    x = 0
    while (input()!= 'no'):
        x += 5
        print(df.head(x))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
