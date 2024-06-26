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
    city = None
    while city not in ["chicago", "new york city", "washington"]:
        city = input("Please choose city: ")
        city = city.lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = None
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Please choose month: ")
        month = month.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    while day not in ['all','Monday','Tuesday','Wednesday','Thuesday','Friday','Saturday', 'Sunday']:
        day = input("Please choose weekday: ")
        
        day = day.lower().capitalize()
        if day == "All":
            day = "all"

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

def print_raw_data(df):
    count_num = 0
    while True:
        show_raw_data = input('See 5 lines of raw data? ')
        if show_raw_data.lower() == 'yes':
            print(df[count_num:count_num+5])
            count_num += 5
        else:
            break
    print()

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Display the most common month.")
    print(df['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print("Display the most common day of week.")
    print(df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    print("Display the most common start hour")
    df['hour'] = df['Start Time'].dt.hour
    print(df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print_raw_data(df)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("display most commonly used start station:")
    print(df['Start Station'].value_counts().idxmax())
    
    # TO DO: display most commonly used end station
    print("display most commonly used end station:")
    print(df['End Station'].value_counts().idxmax())


    # TO DO: display most frequent combination of start station and end station trip
    print("display most frequent combination of start station and end station trip")
    df['Station_combine'] = df['Start Station'] + "-" + df['End Station']
    print(df['Station_combine'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print_raw_data(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("display total travel time:")
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("display mean travel time:")
    print(df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print_raw_data(df)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Display counts of user types:")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print("Display counts of gender:")
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("Display earliest, most recent, and most common year of birth:")
    print(f"Most earliest year: {df['Birth Year'].min()}")
    print(f"Most recent year: {df['Birth Year'].max()}")
    print(f"Most common year: {df['Birth Year'].value_counts().idxmax()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print_raw_data(df)

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
         
        # set one change

if __name__ == "__main__":
	main()
