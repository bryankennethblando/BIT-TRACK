import requests
import pandas as pd

# setting up the url connection
url = url = "https://api.binance.com/api/v3/ticker/price"
response = requests.get(url)

# fetching the data in json format
data = response.json()

# insetring the json file into dataframe
df = pd.DataFrame(data)

# to get the values of the top10 coins
df['price'] = pd.to_numeric(df['price'])
top_10_df= df.sort_values(by='price', ascending=False).head(10)

# to saved the dataframe into a csv file
top_10_df.to_csv("data/crypto_data.csv", index=False)
print("Saved Binance data to CSV!")
