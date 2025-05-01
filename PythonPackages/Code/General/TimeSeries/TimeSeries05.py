dh = dg.copy()

from statsmodels.tsa.api import ExponentialSmoothing
from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler(feature_range = (0.00001,1))
dh['scal'] = sc.fit_transform(dh)

model = ExponentialSmoothing(dh['scal'], trend='add',  seasonal='add',
use_boxcox=False, seasonal_periods=26)

dmodel = model.fit(
    smoothing_level = 0.1,
    smoothing_trend = 0.5,
    smoothing_seasonal = 0.1,
    optimized=False
    )

# dmodel = model.fit()
dhfc = pd.DataFrame(dmodel.forecast(60), columns=['forecast'])
dhfc['forecast'] = sc.inverse_transform([dhfc.loc[:,'forecast'].tolist()])[0,:]

dh['fitted'] = sc.inverse_transform([dmodel.fittedvalues.tolist()])[0,:]