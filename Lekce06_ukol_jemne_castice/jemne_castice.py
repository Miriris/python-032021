import pandas
import requests
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

air_polution = pandas.read_csv("air_polution_ukol.csv")
print(air_polution.head())

air_polution["date"] = pandas.to_datetime(air_polution["date"])


air_polution["year"] = air_polution["date"].dt.year
air_polution["month"] = air_polution["date"].dt.month
air_polution["month and year"] = air_polution["month"].astype(str) + "/" + air_polution["year"].astype(str)

print(air_polution.head())

air_polution = air_polution.dropna()

print(air_polution.head())

#nulová hypotéza - průměrné množství polétavých částic je stejné
#alternativní hypotéza - průměrné množství polétavých částic není stejné

x = air_polution[air_polution["month and year"] == "1/2019"]["pm25"]
y = air_polution[air_polution["month and year"] == "1/2020"]["pm25"]

print(mannwhitneyu(x, y))

#nulovou hypotézu zamítám, průměrné množství polétavých částic v lednu roku 2019 a 2020 není stejné.
