import pandas as pd
import seaborn as sns
import os


class Stats:
    def __init__(self, city_name):
        self.city_name = city_name
        
    
    def load_data(self):
        """
        Args:
            name (string): Name of the csv file.
        This function takes the name of csv file as an input and do some modification for
        computing the relevant statistics.
        Returns:
            df- The modified dataframe
        """
        df_path = os.getcwd()
        file_name = self.city_name+".csv"
        new_path = os.path.join(df_path,"data", file_name)
        df = pd.read_csv(new_path)
        
        # Convert start time to datetime
        df["Start Time"] = pd.to_datetime(df["Start Time"])
        
        df['End Time'] = pd.to_datetime(df['End Time'])
        
        # extract hour, month and week_day from the Start Time
        df["hour"] = df['Start Time'].dt.hour
        df["day_of_week"] = df['Start Time'].dt.day_name()
        df["month"] = df['Start Time'].dt.month
        df["year"] = df["Start Time"].dt.year
        
        return df
    
    def popular_time_hours(self):
        
        """
        This function tells about the most common month, day of week, hour of day
        depending on the start time
        """
        data = self.load_data()
        fig1 = sns.barplot(x=data["hour"].value_counts().index\
                           ,y=data["hour"].value_counts())
        fig1.set(xlabel='Hours', ylabel='Counts')    
        return fig1
    
    def popular_time_days(self):
        
        """
        This function tells about the most common month, day of week, hour of day
        depending on the start time
        """
        data = self.load_data()
        fig1 = sns.barplot(x=data["day_of_week"].value_counts().index\
                           ,y=data["day_of_week"].value_counts())
            
        fig1.set(xlabel='Days', ylabel='Counts')
            
        fig1.set_xticklabels(fig1.get_xticklabels(), 
                          rotation=45, 
                          horizontalalignment='right')
        return fig1
    
    def popular_time_months(self):
        
        """
        This function tells about the most common month, day of week, hour of day
        depending on the start time
        """
        data = self.load_data()
        fig1 = sns.barplot(x=data["month"].value_counts().index\
                           ,y=data["month"].value_counts())
            
        fig1.set(xlabel='Months', ylabel='Counts')
        
        return fig1
    
    def popular_trips_stations_stats(self):
        
        """
        This function tells about the most common strt and end points
        most common trip from start to end 
        (i.e., most frequent combination of start station and end station)
        """  
        data = self.load_data()
        # most commonly used start station
        start_station = data['Start Station'].mode().values[0]
        
    
        # most commonly used end station
        end_station = data['End Station'].mode().values[0]
    
    
        data['routes'] = data['Start Station']+ " " + data['End Station']
    
        frequent_route = data['routes'].mode().values[0]
    
    
        return start_station, end_station, frequent_route
    
    
    
    def trip_duration_stats(self):
        
        """
        This function gives total travel time and average travel time
        """
        
        data = self.load_data()
        data['duration'] = data['End Time'] - data['Start Time']

        # display total travel time
        Maximum_distance = str(data['duration'].sum())
        
    
        # display mean travel time
        Average_distance = str(data['duration'].mean())
        
        return Maximum_distance, Average_distance
        
    
    
    def user_info_stats(self):
        
        """
        counts of each user type
        counts of each gender (only available for NYC and Chicago)
        earliest, most recent, most common year of birth (only available for NYC and Chicago
        """
        data = self.load_data()
        fig1 = sns.barplot(x=data["User Type"].value_counts().index\
                           ,y=data["User Type"].value_counts())
            
        fig1.set(xlabel='Users', ylabel='Counts')
        return fig1
                
    def gender_stats(self):
        
        
        data = self.load_data()
        fig1 = sns.barplot(x=data["Gender"].value_counts().index\
                           ,y=data["Gender"].value_counts())
            
        fig1.set(xlabel='Users', ylabel='Counts')
        return fig1
        
    def birth_stats(self):
        
        data = self.load_data()
        earliest_birth = str(int(data['Birth Year'].min()))
        latest_birth = str(int(data['Birth Year'].max()))
        common_birth = str(int(data['Birth Year'].mode().values[0]))
        
        return earliest_birth, latest_birth, common_birth
    

    