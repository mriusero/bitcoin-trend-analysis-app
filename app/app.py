from dashboard.layout import create_layout
from functions.data_processing import load_data

def main():
    market_df = load_data("data/output/Bitcoin_market_historical.csv")
    tweet_df = load_data("data/output/Bitcoin_tweets_historical.csv")

    create_layout(market_df, tweet_df)

if __name__ == '__main__':
    main()
