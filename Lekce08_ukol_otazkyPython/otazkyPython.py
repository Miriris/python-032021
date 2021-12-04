import pandas
import requests
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/MLTollsStackOverflow.csv")
with open("MLTollsStackOverflow.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("MLTollsStackOverflow.csv")
print(df.head())

df_python = pandas.DataFrame(df, columns=["python"])

print(df_python.head())

#decompose = seasonal_decompose(df_python, model="multiplicative", period=12)
#decompose.plot()
#plt.show()

from statsmodels.tsa.holtwinters import ExponentialSmoothing

mod = ExponentialSmoothing(df_python, seasonal_periods=12, trend="add", seasonal="add", use_boxcox=True, initialization_method="estimated")
res = mod.fit()
df["HM"] = res.fittedvalues
#df[["HM", "python"]].plot()
df_forecast = pandas.DataFrame(res.forecast(24), columns=["Prediction"])
df_with_prediction = pandas.concat([df_python, df_forecast])
df_with_prediction[["python", "Prediction"]].plot()
plt.show()



