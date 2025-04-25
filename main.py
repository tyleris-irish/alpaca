import keyring

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestTradeRequest

from cred_mgmt import get_credentials


ENDPOINT = "https://paper-api.alpaca.markets/v2"


def main():
    # Initialize the client
    client = StockHistoricalDataClient(get_credentials("api_key"), get_credentials("api_secret"))

    # Create a request for the latest trade of VOO
    request_params = StockLatestTradeRequest(symbol_or_symbols="VOO")

    # Fetch the latest trade data
    latest_trade = client.get_stock_latest_trade(request_params)

    # Extract and print the latest price
    voo_price = latest_trade["VOO"].price
    print(f"Latest VOO price: ${voo_price:.2f}")


if __name__ == "__main__":
    main()
