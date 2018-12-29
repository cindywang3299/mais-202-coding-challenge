import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/McGillAISociety/mais-202-coding-challenge/master/data.csv')
df1 = df.groupby('purpose')['int_rate'].mean().reset_index()
df1.rename(columns={'int_rate':'avg_rate'}, inplace=True)

df1.set_index("purpose",drop=True,inplace=True)
df

df1.plot.bar()
plt.show()
