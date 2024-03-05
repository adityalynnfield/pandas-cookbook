

# importing pandas
import pandas as pd
#import madplotlib
import matplotlib.pyplot as plt
#.read_csv reads the data from the CSV file 
#1st parameter is relative path for the file
#second parameter is the seperator in the file
#third parameter is the enconding language(default is UTF 8)
#fourth parameter parses the date and puts it in the standard format
#5th parameter makes it so the day is always first
#6th parameter changes the values in the date column
fixed_df = pd.read_csv('../data/bikes.csv',  sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
fixed_df[:3]
#plotting the data
fixed_df['Berri 1'].plot()
fixed_df.plot(figsize = (15,10))