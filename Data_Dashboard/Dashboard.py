import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('/home/hunter/projects/Python_Projects/Data_Dashboard/Data/Amazon stock data 2000-2025.csv')
headers = df.head()
print(headers)
columns = df.columns
print(columns)
for column in columns:
    print(df[column].size)
    plt.plot()