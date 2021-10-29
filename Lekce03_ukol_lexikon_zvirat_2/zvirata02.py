import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

zvirata02 = pandas.read_csv("lexikon-zvirat.csv", sep=";")
#print(zvirata02)

zvirata02 = zvirata02.dropna(how="all", axis="columns")
zvirata02 = zvirata02.dropna(how="all", axis="rows")
zvirata02 = zvirata02.set_index("id")
print(zvirata02.tail(30))

def popisek(radek):
    popisek_zvirete = str(radek.title) + " se živí následujícím typem stravy: " + str(radek.food) + ". Nejvíce ocení, když se v misce objeví " + str.lower(str(radek.food_note)) + ". Jak toto zvíře poznáme: " + str(radek.description) + "."
    return popisek_zvirete

zvirata02["popisek"] = zvirata02.apply(popisek, axis=1)
print(zvirata02.head())

#zvirata02 = zvirata02.reset_index()
#print(zvirata02.iloc[1])
zvirata02.to_csv("zvirata02.csv")
