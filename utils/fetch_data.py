import requests
from config import API_URL, CURRENCY_LIST, TOP_N

def fetch_crypto_data():
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": TOP_N,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        crypto_list = []
        for coin in data:
            crypto_list.append({
                "name": coin["name"],
                "symbol": coin["symbol"],
                "usd": coin["current_price"],
                "inr": coin["current_price"] * 83  # Approx INR conversion
            })
        return crypto_list
    else:
        print("Error fetching data:", response.status_code)
        return []
