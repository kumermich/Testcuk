df = df[df['City']=='Munich']
df = df[['Year', 'Month', 'Day', 'AvgTemperature']]
df = df[df['AvgTemperature']>-70]

df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
df = df.set_index(df['Date'])
df = df[['AvgTemperature']]

df['AvgTemperature'] = (df['AvgTemperature']-32)*5/9

df['AvgTemperature'].plot()
plt.show()

df.info(memory_usage="deep")