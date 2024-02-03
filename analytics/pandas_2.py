import pandas as pd

# load datasets from dict
weather_data ={
    'day':['1/1/2016','1/2/2016','1/3/2016','1/4/2016','1/5/2016'],
    'temperature':[38,30,23,25,32],
    'windspeed':[2,5,8,7,5],
    'event':['Sunny','Rainy','Snow','Snow' ,'Sunny']
}

df = pd.DataFrame(weather_data)
print(df)

# get rows and columns of Dataframe
print(df.shape)

print(df.columns)

# get column : df.day / df['day']
print(df.day)
print(df.temperature)

# print only required columns
print(df[['day', 'event']])

# statistics
print("Stat data : ",df['temperature'].std())

# get row by index
print(df.iloc[[2]])