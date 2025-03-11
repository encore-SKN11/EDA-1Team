import numpy as np
import pandas as pd


data = pd.read_csv('./data/baseball_stats_2024.csv')

df = pd.DataFrame(data)
print(df)