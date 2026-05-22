import requests
import pandas as pd

def update_data():

    print("Fetching fresh data from API....")
    url = "https://api.binance.com/api/v3/ticker/price"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data)

        df['price'] = pd.to_numeric(df['price'])
        top_10_df= df.sort_values(by='price', ascending=False).head(10)

        top_10_df.to_csv("data/crypto_data.csv", index=False)
        print("Successfully updated crypto_data.csv!")
        return True
    else:
        print("Failed to Fetch data")
        return


