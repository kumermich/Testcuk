from pathlib import Path

url = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1121068/milkutil-dataset-01dec22.ods'

!wget $url

fn = Path(url).name

!libreoffice --headless --convert-to csv $fn

# skip 8 lines
# superscript numbers in column 2
# engine='python': required for: skipfooter=10
# rename header: names = ['Date', 'Milk'], header = 0,

df = pd.read_csv(fn,
        skiprows=8, skipfooter=9,
        usecols=[0,5], names = ['Date', 'Milk'], header = 0,
        parse_dates=['Date'], index_col='Date',
        encoding = "ISO-8859-1", engine='python')

df = df.resample('M').mean()
df.info()