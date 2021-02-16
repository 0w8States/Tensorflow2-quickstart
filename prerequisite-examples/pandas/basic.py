# Basic sample of importing, modifying, and exporting dataframes
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

df = pd.read_csv('sbux.csv')

# export only the open and close price columns
smalldf = df[['open', 'close']]
smalldf.to_csv('output.csv')

# apply a function to pull the year from the timestamp
def date_to_year(row):
  return int(row['date'].split('-')[0]) # select only the year, 0th element in this case

# does something similar to a for loop, and accepts a function
df['year'] = df.apply(date_to_year, axis=1)

# Export witht he new year column
df.to_csv('new_sbux.csv')

# Plot the data on historgram
#df['open'].hist()


# Plot the data on line
#df['open'].plot()

# Box Plot
#df[['open', 'high', 'low', 'close']].plot.box()

# Scatter matrix shows the linear correlation between the columns
# Good for looking at how the data is related to one another
scatter_matrix(df[['open', 'high', 'low', 'close']], alpha=0.2, figsize=(6,6) )
plt.show()