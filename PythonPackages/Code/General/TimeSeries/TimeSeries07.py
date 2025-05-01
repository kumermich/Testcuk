from statsmodels.tsa.api import ExponentialSmoothing
from sklearn.preprocessing import MinMaxScaler

dh = df.copy()

sc = MinMaxScaler(feature_range = (0.00001,1))
dh['scal'] = sc.fit_transform(dh)

model = ExponentialSmoothing(dh['scal'], trend='add',  seasonal='add', use_boxcox=True, seasonal_periods=12)

dmodel = model.fit()

dh['fitted'] = sc.inverse_transform([dmodel.fittedvalues.tolist()])[0,:]
dhfc = pd.DataFrame(dmodel.forecast(36))
dhfc['forecast'] = sc.inverse_transform([dhfc.iloc[:,0].tolist()])[0,:]