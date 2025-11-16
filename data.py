import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# time
end = dt.datetime.now()
start = dt.datetime(2000,1,1)

# stock name (.AX)
stocks = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN", "META", "NFLX"]  # US Stocks
stocks += ["CBA.AX", "NAB.AX", "ANZ.AX"]  # Australian Stocks
stocks += ["7203.T", "6758.T", "9984.T"]  # Japanese Stocks (Toyota, Sony, SoftBank)

# fetch its stock data
df = yf.download(stocks, start=start, end=end)
print(df.head())

returns = df['Close'].pct_change()
plt.figure(figsize=(12,6))

for stock in stocks:
    plt.plot(df['Close'][stock],label=stock)
# Plot 
plt.title("stock prices over time")
plt.xlabel("Year")
plt.ylabel("Stock Price (AUD)")
plt.legend()
plt.show()
