import yfinance as yf
import datetime

startDate = datetime.datetime(2022, 1, 1)
endDate = datetime.datetime(2022, 10, 4)

GetFacebookInformation = yf.Ticker("META")

print(GetFacebookInformation.history(start=startDate, end=endDate))