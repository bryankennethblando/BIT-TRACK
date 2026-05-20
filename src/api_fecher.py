import requests
import pandas as pd

url = url = "https://api.binance.com/api/v3/ticker/price"
response = requests.get(url)

data = response.json()
df = pd.DataFrame(data)

df['price'] = pd.to_numeric(df['price'])
top_10_df= df.sort_values(by='price', ascending=False).head(10)

top_10_df.to_csv("data/crypto_data.csv", index=False)
print("Saved Binance data to CSV!")
