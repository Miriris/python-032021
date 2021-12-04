import yfinance as yf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.ar_model import AutoReg
import pandas
import matplotlib.pyplot as plt

csco = yf.Ticker("CSCO")
csco_df = csco.history(period="5y")

print(csco_df.head())

csco_close = pandas.DataFrame(csco_df, columns=["Close"])

print(csco_close.head())
#print(csco_close.tail(25))
print(csco_close["Close"].autocorr(1))

#plot_acf(csco_close)
#plt.show()

#csco_close.plot()
#plt.show()

model = AutoReg(csco_close, lags=20)
res = model.fit()
prediction = res.predict(start=csco_close.shape[0], end=csco_close.shape[0] + 5)
df_prediction = pandas.DataFrame(prediction, columns=["Prediction"])
csco_close_last = csco_close.loc["2021-10-02"::]
df_with_prediction = pandas.concat([csco_close_last, df_prediction])
df_with_prediction.plot()
plt.show()





