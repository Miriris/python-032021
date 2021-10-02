import pandas
import requests
import matplotlib.pyplot as plt
import numpy


r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

df_passengers = pandas.read_csv("titanic.csv")
print(df_passengers.head())

#print(df_passengers.dtypes)

df_passengers["Class/sex"] = df_passengers["Pclass"].astype(str) + " " + df_passengers["Sex"]
df_passengers["Survived/index"] = df_passengers["Survived"].astype(str)

print(df_passengers.head())

df_passengers_pivot = pandas.pivot_table(df_passengers, values="Survived", index="Class/sex", columns="Survived/index", aggfunc=len, margins=True)

print(df_passengers_pivot)



