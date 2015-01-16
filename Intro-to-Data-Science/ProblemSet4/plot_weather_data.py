import pandas 
from ggplot import *
import dateutil

def plot_weather_data(df):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    #df['datetime'] = pandas.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S')
    #df['datetime'] = df['datetime'].astype('datetime64[ns]')
    #df = df.sort('datetime')
    #print df
    #df['datetime'] = df['datetime'].apply(dateutil.parser.parse)

    plot = ggplot(df, aes('EXITSn_hourly', 'ENTRIESn_hourly', color='rain')) + geom_point() + ggtitle("Entries vs Exits") + xlab("Exits") + ylab("Entries")
    
    return plot


