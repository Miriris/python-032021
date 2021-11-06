import pandas
from scipy.stats import mannwhitneyu
import requests

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
  open("psenice.csv", 'w', encoding="utf-8").write(r.text)


psenice_df = pandas.read_csv("psenice.csv")
print(psenice_df.head())

#nulová hypotéza - délka zrn je rovná
#alternativní hypotéza - délka zrn není rovna

x = psenice_df["Rosa"]
y = psenice_df["Canadian"]

print(mannwhitneyu(x, y, alternative="greater"))

#Nulovou hypotézu zamítám: platí, že zrna nejsou rovna.
