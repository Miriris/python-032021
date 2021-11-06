import pandas
import requests
import matplotlib.pyplot as plt
import seaborn

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

krypto = pandas.read_csv("crypto_prices.csv")
print(krypto.head())
#print(krypto.dtypes)



krypto["Pct_change"] = krypto.groupby("Symbol")["Close"].pct_change()
krypto_pivot = pandas.pivot(krypto, values="Pct_change", index="Date", columns="Symbol")
print(krypto_pivot.head())

print(krypto_pivot.corr())

#seaborn.jointplot("ADA", "UNI", krypto_pivot, kind="scatter")
#plt.show()

seaborn.jointplot("ADA", "DOGE", krypto_pivot, kind="scatter")
plt.show()