import pandas
import numpy

import requests

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
  open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)


president_elections = pandas.read_csv("1976-2020-president.csv")
#print(president_elections.head())

president_elections = president_elections.sort_values(["state", "year"])
#print(president_elections.head())

president_elections["poradi"] = president_elections.groupby(["state", "year"])["candidatevotes"].rank(method="min", ascending=False)
#print(president_elections.head())


president_elections = (president_elections[(president_elections["poradi"] == 1.0)])
#print(president_elections)

president_elections["party_simplified_previous"] = president_elections["party_simplified"].shift(periods=-1)
print(president_elections)

president_elections = president_elections.dropna(subset=["party_simplified_previous"])
print(president_elections)

president_elections["change"] = numpy.where(president_elections["party_simplified"] == president_elections["party_simplified_previous"], "1", "0")
print(president_elections)

president_elections_swing = president_elections[(president_elections["change"] == "0")]
president_elections_swing = president_elections_swing.groupby(["state"]).sum()
print(president_elections_swing)

president_elections_swing = president_elections_swing.sort_values(by=(["poradi", "state"]), ascending=False)
print(president_elections_swing)




