"""
--------------------------------------------------------
SOC Week 1

Yahoo Finance API Example

Objective:
Download recent Copper Futures prices using
Yahoo Finance API and save the data as CSV.
--------------------------------------------------------
"""

import yfinance as yf
import pandas as pd

# Copper Futures ticker
ticker = "HG=F"

print("=" * 50)
print("Fetching Copper Futures Data...")
print("=" * 50)

# Download last 5 days of data
copper = yf.Ticker(ticker)
data = copper.history(period="5d")

print(data)

# Save data
data.to_csv("yahoo_finance_data.csv")

print("\nData saved as yahoo_finance_data.csv")