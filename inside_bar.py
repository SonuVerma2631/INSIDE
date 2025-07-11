import yfinance as yf
import pandas as pd

with open("fnolist.txt") as f:
    symbols = [line.strip() for line in f if line.strip()]

inside_bar = []

for symbol in symbols:
    try:
        data = yf.download(symbol, interval="1d", period="3d")
        if len(data) >= 2:
            prev = data.iloc[-2]
            curr = data.iloc[-1]
            
            if curr["High"] < prev["High"] and curr["Low"] > prev["Low"]:
                inside_bar.append({
                    "Stock": symbol,
                    "Prev High": round(prev["High"], 2),
                    "Curr High": round(curr["High"], 2),
                    "Prev Low": round(prev["Low"], 2),
                    "Curr Low": round(curr["Low"], 2)
                })
    except:
        pass

df = pd.DataFrame(inside_bar)
df.to_excel("Inside_Bar_Screener.xlsx", index=False)
print(f"✅ Found {len(inside_bar)} stocks with inside bar pattern.")