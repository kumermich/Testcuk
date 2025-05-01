from datetime import datetime

fn = 'data/energy-charts_Total_net_electricity_generation_in_Germany.csv'

my_date_parser = lambda x: datetime.strptime(x, "%m.%Y")

df = pd.read_csv(fn, index_col='Month', usecols=['Month', 'Solar'],
                 parse_dates=['Month'], date_parser =  my_date_parser)
df.index.name='Date'

#drop last value (incomplete information about last month)
df = df.iloc[:-1,:]

resamp = 'M'
df = df.resample(resamp).mean()

print('Missing for resampling period ', resamp, ': ',
         int(df.loc[:, :].isnull().sum()) )