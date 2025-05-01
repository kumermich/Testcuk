# source: https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities
fn = 'data/city_temperature.zip'
df = pd.read_csv(fn, dtype={'State':object}, compression='zip')
df.info(memory_usage="deep")