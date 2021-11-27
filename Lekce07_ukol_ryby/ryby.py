import pandas
import requests
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
  f.write(r.content)


df = pandas.read_csv("Fish.csv")
print(df.head())
print(df.columns)

#mod = smf.ols(formula="Weight ~ Length2 + Height", data=df)
#res = mod.fit()
#print(res.summary())

#r-squared no1 = 0.844 no2 = 0.875 - kvalita se zvýšila o 3,1%.

average = df.groupby("Species")["Length2"].mean()
df["Average_by_species"] = df["Species"].map(average)

mod = smf.ols(formula="Weight ~ Length2 + Height + Average_by_species", data=df)
res = mod.fit()
print(res.summary())
