import pandas as pd

df = pd.read_csv('./datasets/nyc_weather.csv')

# print the dataframe head  [5 rows]
print(df.head())

# print the max temperature
print(df['Temperature'].max())

# print the days where it rained
print(df['EST'][df['Events']=='Rain'])

# mean WindSpeedMPH
df.fillna(0, inplace=True)
print(df['WindSpeedMPH'].mean())