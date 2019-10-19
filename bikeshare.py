import time
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

CITY_DATA = { 'chicago': 'C:\\Users\\varun\\OneDrive\\Udacity\\chicago.csv',
              'new york city': 'C:\\Users\\varun\\OneDrive\\Udacity\\new_york_city.csv',
              'washington': 'C:\\Users\\varun\\OneDrive\\Udacity\\washington.csv' }

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
    while True:
        city=input('Enter the name of city: ')
        if city.lower() not in ('chicago','new york city','washington'):
            print('City not in list. Please re-enter again')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Enter the month name you want to analyze: ')
        if month.lower() not in ('january','february','march','april','may','june','july','august','september','october','november','december','all'):
            print('Month invalid. Please re-enter again')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Enter the day name you want to analyze: ')
        if day.lower() not in ('sunday','monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            print('Day invalid. Please re-enter again')
        else:
            break
    print('-'*40)
    print('Per selection, you want to aggregate for {}, {} month(s) and {} day(s)'.format(city,month,day))
    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    
    # filling the data set with CSV file
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['monthno'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        monthno = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['monthno'] == monthno]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    try:
        
        # TO DO: display the most common month
        most_common_month = df['monthno'].value_counts().idxmax()
        print('Most Common month for travel is ' + str(most_common_month))
    
        # TO DO: display the most common day of week
        most_common_week = df['day_of_week'].value_counts().idxmax()
        print('Most Common week for travel is ' + str(most_common_week))

        # TO DO: display the most common start hour
        most_common_hour = df['hour'].value_counts().idxmax()
        print('Most Common hour for travel is ' + str(most_common_hour))

        print("\n\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
    except:
        print('\n\nColumns not found\n\n')
        
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    try:
        # TO DO: display most commonly used start station
        most_common_ss = df['Start Station'].value_counts().idxmax()
        print('Most Common Station where journey started is ' + str(most_common_ss))

        # TO DO: display most commonly used end station
        most_common_es = df['End Station'].value_counts().idxmax()
        print('Most Common Station where journey ended is ' + str(most_common_es))
        
        # TO DO: display most frequent combination of start station and end station trip
        print('Most frequent combination is \n' + str(df.groupby(['Start Station','End Station']).size().nlargest(1)))

        print("\n\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    except:
        print('\n\nColumns not found\n\n')
        
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    try:
        # TO DO: display total travel time
        total_tt = df['Trip Duration'].sum()
        print('Total Trip Duration is ' + str(total_tt))
    
        # TO DO: display mean travel time
        mean_tt=df['Trip Duration'].mean()
        print('Mean Trip Duration is ' + str(mean_tt))
    
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print('\n\nColumns not found\n\n')

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print('User types in data set are \n' + str (user_types))
    
        # TO DO: Display counts of gender
        d_gender = df['Gender'].value_counts()
        print('Gender wise count is \n' + str (d_gender))
        
        # TO DO: Display earliest, most recent, and most common year of birth
        min_birth=df['Birth Year'].min()
        max_birth=df['Birth Year'].max()
        mf_birth=df['Birth Year'].value_counts().idxmax()
        print('\nEarliest Birth Year is {0}, max Birth Year is {1}, Most Frequent Birth Year is {2}'.format(min_birth,max_birth,mf_birth))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print('\n\nColumns not found\n\n')

def main():
    """Code Called when function execution starts"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(len(df))
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        #while loop for looping through dataset
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
          
def raw_data(df):
    """Displaing RAW data of data set"""
    i=0
    dflength=len(df)
    #print(dflength)
    while (i+5)<dflength:
        print(df.iloc[i:i+5]) 
        pr_data=input('Would you want to print data? ')
        if (pr_data=='y' or pr_data=='Y'):
            i=i+5
        else:
            break
    if (i+5)>dflength:
       print(df.iloc[i:dflength])
if __name__ == "__main__":  
    """this is called automatically when py execution statrs"""
	main()