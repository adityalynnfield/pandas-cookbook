import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012 = pd.read_csv('../data/weather_2012.csv', parse_dates=True, index_col='Date/Time')
weather_2012[:5]
weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')
#is_snowing=is_snowing.astype(float)
#is_snowing.plot()
#is_snowing.astype(float).resample('M').apply(np.mean).plot(kind = 'bar')

temperature = weather_2012['Temp (C)'].resample('M').apply(np.median)
is_snowing = weather_2012['Weather'].str.contains('Snow')
snowiness = is_snowing.astype(float).resample('M').apply(np.mean)
temperature.name = "Temperature"
snowiness.name = "Snowiness"

stats = pd.concat([temperature, snowiness], axis=1)
#stats.plot(kind='bar')
stats.plot(kind='bar', subplots=True, figsize=(15, 10))