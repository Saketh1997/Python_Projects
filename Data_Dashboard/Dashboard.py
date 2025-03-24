import pandas as pd
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('/home/hunter/projects/Python_Projects/Data_Dashboard/Data/Amazon stock data 2000-2025.csv')

headers = df.head()
# pattern = re.compile(r'(\d+)\-(\d+)\-(\d+)\s(\d+)\:(\d+)\:(\d+)\-(\d+)\:(\d+)')
# print(df.dtypes)
# for date in df['date']:
#     matching = pattern.search(date)
#     if matching:
#         newDate = matching.group(1) + ' - ' + matching.group(2) + ' - '+ matching.group(3)
#         date = newDate

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S%z', utc=True)
df['date'] = df['date'].dt.year.astype(str) + '/' + df['date'].dt.month.astype(str) + '/' + df['date'].dt.day.astype(str) 
df.to_csv('/home/hunter/projects/Python_Projects/Data_Dashboard/Data/Amazon_stock_data_modified.csv', index=False)

plt.figure(figsize=(60, 6))

plt.plot(df['date'][::100], df['open'][::100] ,marker='x', linestyle='-', label='Open')
plt.plot(df['date'][::100], df['close'][::100] ,marker='x', linestyle='-', label='Close')
plt.title("Amazon's stock price graph")
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.savefig('stock_prices.png')