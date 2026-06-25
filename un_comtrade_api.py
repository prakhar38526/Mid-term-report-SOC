import requests
import pandas as pd

url = "https://comtradeapi.worldbank.org/data/v1/get/C/A/HS"

params = {
    "reporterCode": "840",
    "partnerCode": "156",
    "cmdCode": "260300",
    "flowCode": "M",
    "period": "2023"
}

print("=" * 50)
print("Fetching UN Comtrade Data...")
print("=" * 50)

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    records = data.get("data", [])

    if records:
        df = pd.DataFrame(records)
        print(df.head())
        df.to_csv("un_comtrade_data.csv", index=False)
        print("\nData saved as un_comtrade_data.csv")
    else:
        print("No records returned from the API.")

except requests.exceptions.RequestException as e:
    print("Unable to fetch data from the UN Comtrade API.")
    print("Reason:", e)