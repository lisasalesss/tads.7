import plotly.express as px
from data.download import download_data

data = download_data('BBAS3.SA')

data[['Close']]
data['SMA'] = data['Close'].rolling(window= 9).mean
data['SMA'] = data['Close'].rolling(window= 72).mean