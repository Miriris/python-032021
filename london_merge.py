import pandas
import requests
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)

df_london_merged = pandas.read_csv("london_merged.csv")

df_london_merged["date_converted"] = pandas.to_datetime(df_london_merged["timestamp"])
df_london_merged["year"] = df_london_merged["date_converted"].dt.year
df_london_merged["weather_code/index"] = df_london_merged["weather_code"].astype(str)

#print(df_london_merged.dtypes)
print(df_london_merged.head())

df_london_merged_pivot = pandas.pivot_table(df_london_merged, values="cnt", index="year", columns="weather_code/index", aggfunc=numpy.sum, margins=True)

print(df_london_merged_pivot)

sns.heatmap(df_london_merged_pivot, annot=True, fmt=".3f", linewidths=0.5, cmap="Greens")

plt.show()





