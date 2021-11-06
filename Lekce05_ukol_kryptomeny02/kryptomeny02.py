import statistics

import pandas
import requests
import matplotlib.pyplot as plt
import seaborn

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

krypto = pandas.read_csv("crypto_prices.csv")
print(krypto.head())

krypto["Pct_change"] = krypto.groupby("Symbol")["Close"].pct_change()

#krypto_ETH = krypto[krypto["Symbol"] == "ETH"]
krypto_XMR = krypto[krypto["Symbol"] == "XMR"]

#print(krypto_ETH.head())
print(krypto_XMR.head())

#krypto_ETH["Growth"] = krypto_ETH["Pct_change"] + 1
#print(krypto_ETH.head())
#krypto_ETH = krypto_ETH.dropna()

#seznam = krypto_ETH["Growth"].tolist()

krypto_XMR["Growth"] = krypto_XMR["Pct_change"] + 1
print(krypto_XMR.head())
krypto_XMR = krypto_XMR.dropna()

seznam = krypto_XMR["Growth"].tolist()
print(statistics.geometric_mean(seznam))

