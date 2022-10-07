import yfinance as yf
import plotly.graph_objs as go
import datetime

#startDate = datetime.datetime(2022, 9, 20)
#endDate = datetime.datetime(2022, 10, 6)
#GetFacebookInformation = yf.Ticker("META")
#print(GetFacebookInformation.history(start=startDate, end=endDate))

choice = input("Write a stock symbol: ")
choice = choice.upper()

data = yf.download(tickers=choice, period = '30d', interval = '1d', rounding=True)

fig = go.Figure()

fig.add_trace(go.Candlestick(x=data.index,open = data['Open'],
high=data['High'], low=data['Low'], close=data['Close'],
name = 'market data'))

fig.update_layout(title = choice + ' share price ', 
yaxis_title = 'Stock Price (USD)')

fig.update_xaxes(
    rangeslider_visible=True
)

fig.show()