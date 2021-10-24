import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

import requests


with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

air_polution = pandas.read_csv("air_polution_ukol.csv")
print(air_polution.head())

air_polution["date"] = pandas.to_datetime(air_polution["date"])
print(air_polution.head())
#print(air_polution.dtypes)

air_polution["year"] = air_polution["date"].dt.year
air_polution["month"] = air_polution["date"].dt.month
#print(air_polution.head())
#print(air_polution.tail())

air_polution_pivot = pandas.pivot_table(air_polution, values="pm25", index="month", columns="year", aggfunc=numpy.mean)

print(air_polution_pivot)

#dobrovolné
#graf
sns.heatmap(air_polution_pivot, annot=True, fmt=".1f", linewidths=.5, cmap="Greens")
plt.show()

#dny v týdnu
air_polution["day_of_week"] = air_polution["date"].dt.dayofweek
print(air_polution.head(25))

air_polution_po_dnech_pivot = pandas.pivot_table(air_polution, values="pm25", index="day_of_week", aggfunc=numpy.mean)
print(air_polution_po_dnech_pivot)
