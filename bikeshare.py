import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input("Please specify one the city to analyze (chicago/new york city/washington): ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Only three cities available: chicago, new york city, washington. Please try again: ").lower()
    month = input("Please specify - name of the month to filter by, or 'all' to apply no month filter: ").lower()
    day = input("Please specify - name of the weekday to filter by, or 'all' to apply no day filter: ").lower()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    CITY_DATA = { 'chicago': 'chicago.csv',
                  'new york city': 'new_york_city.csv',
                  'washington': 'washington.csv' }

    df = pd.read_csv(CITY_DATA[city])
    df['Month'] = pd.to_datetime(df['Start Time']).dt.strftime('%B')
    df['Weekday'] = pd.to_datetime(df['Start Time']).dt.strftime('%A')

    if month != 'all': df = df[df['Month']==month.title()]
    if day != 'all': df = df[df['Weekday']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Starthour'] = pd.to_datetime(df['Start Time']).dt.strftime('%H')
    Month = df["Month"].value_counts()[:1].index.tolist()[0]
    Day = df["Weekday"].value_counts()[:1].index.tolist()[0]
    Hour = df["Starthour"].value_counts()[:1].index.tolist()[0]

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour
    print('Most common month: {}'.format(Month))
    print('Most common day of week: {}'.format(Day))
    print('Most common start hour: {}'.format(Hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip
    df['StationComb'] = df[['Start Station', 'End Station']].agg('-'.join, axis=1)
    Sstation = df["Start Station"].value_counts()[:1].index.tolist()[0]
    Estation = df["End Station"].value_counts()[:1].index.tolist()[0]
    Comb = df["StationComb"].value_counts()[:1].index.tolist()[0]

    print('Most common ending station: {}'.format(Estation))
    print('Most common start station: {}'.format(Sstation))
    print('Most common start station and end station: {}'.format(Comb))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time
    print("Total travel time: " + str(sum(df['Trip Duration'])))
    print("Average travel time: " + str(np.average(df['Trip Duration'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types")
    print(df["User Type"].value_counts())

    # TO DO: Display counts of gender
    print("Counts of user types")
    if 'Gender' in df.columns:
        print(df["Gender"].value_counts())
    else:
        print('No Gender Info')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earliest year of birth: " + str(min(df['Birth Year'])))
        print("Most recent year of birth: " + str(max(df['Birth Year'])))
        print("Most common year of birth: " + str(df["Birth Year"].mode()[0]))
    else:
        print('No Birth Year Info')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        n = 0
        dataflag = input('\nWould you like to see more data? Enter yes or no.\n').lower()
        while dataflag == 'yes':
            print(df[n:n+5])
#             print('Printing ' + str(n) + 'rows.')
            n = n + 5
            dataflag= input('\nWould you like to see more data? Enter yes or no.\n').lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
