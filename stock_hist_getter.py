import yfinance as yf
import numpy as np
"""
Author: Rishabh Viswanathan

Creates a CSV for the stock data needed for the UCSD DS3 Stock Group A project. 
"""

def hist_getter(tickers, days):
    """
    Gives the open, high, low, and close prices for the given tickers in the
    past given number of trading days. Also gives the volume of shares traded
    for each day.
    """
    ticks, hists = [], []
    for i in tickers:
        ticks.append(yf.Ticker(i))
    for j in ticks:
        hists.append(j.history(period = "{}d".format(days)))
    for i in range(days):
        s = '';
        for j in hists:
            s += ('{}, {}, {}, {}, {}'.format(
                j['Open'][i],
                j['High'][i],
                j['Low'][i],
                j['Close'][i],
                j['Volume'][i]))
            s += ', '
        print(s)


t = ["FB", "AAPL", "AMZN", "NFLX", "GOOGL", "TSLA"]
