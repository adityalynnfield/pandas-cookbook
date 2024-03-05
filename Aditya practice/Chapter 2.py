import pandas as pd
import matplotlib.pyplot as plt

complaints = pd.read_csv('../data/311-service-requests.csv', dtype='unicode')
# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

complaints['Complaint Type']
complaints[:5]
complaints['Complaint Type'][:5]
complaints[['Complaint Type', 'Borough']][:10]

complain_count = complaints['Complaint Type'].value_counts()
complain_count[:10].plot(kind='bar')
