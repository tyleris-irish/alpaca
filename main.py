import keyring

from datetime import datetime
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

from cred_mgmt import get_credentials


ENDPOINT = "https://paper-api.alpaca.markets/v2"


def main():
    # Initialize the client
    client = CryptoHistoricalDataClient(get_credentials("api_key"), get_credentials("api_secret"))

    # Creating request object
    request_params = CryptoBarsRequest(
        symbol_or_symbols=["BTC/USD"],
        timeframe=TimeFrame.Day,
        start=datetime(2025, 1, 1),
        end=datetime(2025, 1, 7)
    )

    # Retrieve daily bars for Bitcoin in a DataFrame and printing it
    btc_bars = client.get_crypto_bars(request_params)

    # Convert to dataframe
    btc_bars.df

    print(btc_bars.df)


if __name__ == "__main__":
    main()
