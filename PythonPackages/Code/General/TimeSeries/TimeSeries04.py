dg = df.copy()

# daily distance
resamp = 'D'
dg = dg.resample(resamp).mean()
print('Missing: ', resamp, ': ', int(dg.loc[:, :].isnull().sum()) )

# two week distance
resamp = '2W'
dg = dg.resample(resamp).mean()
print('Missing: ', resamp, ': ', int(dg.loc[:, :].isnull().sum()) )

# interpolate missing values
dg = dg.interpolate(method='linear')
print('Missing: ', resamp, ': ', int(dg.loc[:, :].isnull().sum()) )