import pandas
import requests
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn


r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
with open("Concrete_Data_Yeh.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("Concrete_Data_Yeh.csv")
print(df.head())
print(df.columns)

mod = smf.ols(formula="csMPa ~ age + cement + slag + flyash + water + superplasticizer + coarseaggregate + fineaggregate", data=df)
res = mod.fit()
print(res.summary())
#print(df.isna().sum())

#Hodnota R-squared koeficientu 0.616 vypovídá o pouze něco málo větší kvalitě modelu než průměr.
# negativně ovlivňuje sílu betonu obsažené množství vody.


