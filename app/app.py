from dashboard.functions import load_csv
from dashboard import app_layout

def main():
    """
    Main function to load data and start the Streamlit app layout.

    This function loads the historical market and tweet data by calling 
    `load_csv` and then passes the data to `app_layout` for rendering the 
    different pages of the dashboard.

    The `load_csv` function loads CSV files containing Bitcoin market data 
    and tweet history, which are then passed to the app layout for display.
    """
    market_data = load_csv("data/output/Bitcoin_market_historical.csv")
    tweet_data = load_csv("data/output/Bitcoin_tweets_historical.csv")

    app_layout(market_data, tweet_data)

if __name__ == '__main__':
    main()
