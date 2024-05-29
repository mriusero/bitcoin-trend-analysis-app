from dashboard.functions import load_csv
from dashboard import app_layout

def main():

    market_data = load_csv("data/output/Bitcoin_market_historical.csv")
    tweet_data = load_csv("data/output/Bitcoin_tweets_historical.csv")

    app_layout(market_data, tweet_data)

if __name__ == '__main__':
    main()
