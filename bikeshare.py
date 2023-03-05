import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)



def check_input(input_str,input_type) :
    while True:
        input_read=input(input_str).lower()
        
        try:
            if input_read in ['chicago','new york city','washington'] and input_type==1:
                return input_read
                break
            elif input_read in ['all', 'january', 'february', 'march', 'april', 'may', 'jun'] and input_type==2:
                return input_read
                break
            elif input_read in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'fraiday', 'satarday'] and input_type==3:
                return input_read
                break
            else:
                if input_type==1:
                    print('wrong city')
                if input_type==2:
                    print('wrong month')
                if input_type==3:
                    print('wrong day')
        except ValueError:
            print('sorry error input')
            
            
            
def get_filters():
    city = check_input('Please enter acity:\n chicago, new york city, washington?\n', 1)
    month = check_input('Please enter amonth:\n from january to jun or all?\n', 2)
    day = check_input('Please enter aday?\n', 3)
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january','february','march','april','may','jun']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[ df['day'] == day.title()]
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(df['month'].mode()[0])

    # TO DO: display the most common day of week
    print(df['day'].mode()[0])

    # TO DO: display the most common start hour
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    print(group_field.size().sort_values(ascending=False).head(1))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration']. sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    if city != 'washington':
        print(df['Gender'].value_counts())
        print(df['Birth Year'].mode()[0])
        print(df['Birth Year'].max())
        print(df['Birth Year'].min())
    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)



        start_index = 0
        end_index = start_index + 5
        invalid_input = True
        while invalid_input:  # to validate user input
            ask_raw_data = input('\nWould you like to See the Raw Data? Enter yes or no.\n').lower()
            if ask_raw_data not in ['yes', 'no']:
                print('Invalid input, please Enter "Yes or No"!')
            elif ask_raw_data == 'yes':
                while True:  # to continuously displaying the Raw data as long as user needed to
                    raw_data = df.iloc[start_index:end_index]
                    print(raw_data)
                    while True:  # to validate user input
                        ask_for_more = input('\nWould you like to See More Data? Enter yes or no.\n')
                        if ask_for_more not in ['yes', 'no']:
                            print('Invalid input, please Enter "Yes or No"!')
                        else:
                            break
                    if ask_for_more == 'yes':
                        start_index += 5
                        if start_index + 5 >= df.shape[0] - 1:  # check for the end of data
                            end_index = df.shape[0]
                            raw_data = df.iloc[start_index:end_index]
                            print(raw_data)
                            print("\nThat is the End of the file")
                            invalid_input = False
                            break
                        else:
                            end_index = start_index + 5
                    else:
                        invalid_input = False
                        break
            else:
                invalid_input = False
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
