from utils.fetch_data import fetch_crypto_data  # Change import to match function name
from config import TOP_N

def main():
    print("\nTop Cryptocurrencies:\n")
    crypto_data = fetch_crypto_data()  # Use correct function name

    for coin in crypto_data:
        print(f"{coin['name']} ({coin['symbol'].upper()}) - USD: ${coin['usd']} | INR: ₹{coin['inr']}")

if __name__ == "__main__":
    main()
