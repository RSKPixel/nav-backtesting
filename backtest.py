import pandas as pd



# df = pd.read_csv("/Users/saravanakumar/Dev/nav-backtesting/hdfc-balance.csv")
# df = pd.read_csv("/Users/saravanakumar/Dev/nav-backtesting/icici-nav.csv")
df = pd.read_csv("/Users/saravanakumar/Dev/nav-backtesting/nippon-gold.csv")
# df = pd.read_csv("/Users/saravanakumar/Dev/nav-backtesting/ppfa.csv")

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')
df = df.set_index('date')

yearly = df['nav'].resample('YE').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last'
})

df = yearly.copy()

df["change"] = df["close"] - df["open"]
df["change_percentage"] = df["change"] / df["open"] * 100

df["change_1"] = df["change_percentage"].rolling(window=1).mean()
df["change_3"] = df["change_percentage"].rolling(window=3).mean()
df["change_5"] = df["change_percentage"].rolling(window=5).mean()
df["change_8"] = df["change_percentage"].rolling(window=8).mean()
df["change_10"] = df["change_percentage"].rolling(window=10).mean()


df = df.round(2)

print(df[["change_1", "change_3", "change_5", "change_8", "change_10"]])
print(round(df["change_1"].mean(),2))