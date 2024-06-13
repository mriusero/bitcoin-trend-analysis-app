### Library_


```python
import pandas as pd
from datetime import datetime, timezone
from IPython.display import clear_output
```

### #BTC Market History [dataset A]
#### Origin_
    URL du dataset_   "https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data"
    
    Origin file_      "bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv"  

    



    



#### Shape_


```python
df = pd.read_csv("../input/bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv")
print("\n------ BTC Market History DataFrame ------\n")
df.info()
```

    
    ------ BTC Market History DataFrame ------
    
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4857377 entries, 0 to 4857376
    Data columns (total 8 columns):
     #   Column             Dtype  
    ---  ------             -----  
     0   Timestamp          int64  
     1   Open               float64
     2   High               float64
     3   Low                float64
     4   Close              float64
     5   Volume_(BTC)       float64
     6   Volume_(Currency)  float64
     7   Weighted_Price     float64
    dtypes: float64(7), int64(1)
    memory usage: 296.5 MB


#### Content_

    #Variables_

      * Type "datetime" (1)  
           - timestamp           : start time of time window (60s window), in Unix time
           
      * Type "float" (7) 
           - Open                : open price at start time window
           - High                : high price within time window              
           - Low                 : low price within time window              
           - Close               : close price at end of time window            
           - Volume_(BTC)        : volume of BTC transacted in this window      
           - Volume_(Currency)   : Volume of corresponding currency transacted in this window 
           - Weighted_Price      : Volume Weighted Average Price [VWAP]
           

#### Period_


```python
df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit='s', utc=True)

start_market = df["Timestamp"].min()
end_market = df["Timestamp"].max()
period = end_market - start_market

print(f"\nstart_market (UTC) : {start_market}\nend_market (UTC) : {end_market}\nperiod : {period}")
```

    
    start_market (UTC) : 2011-12-31 07:52:00+00:00
    end_market (UTC) : 2021-03-31 00:00:00+00:00
    period : 3377 days 16:08:00


#### Cleaning_


```python
empty_before = df.isna().sum()
print(f"\nEmpty values (Before cleaning) :\n-------------------------------------\n{empty_before}")

df = df.dropna()

empty_after = df.isna().sum()
print(f"\nEmpty values (After cleaning) :\n------------------------------------\n{empty_after}")

market_df = df.copy()
```

    
    Empty values (Before cleaning) :
    -------------------------------------
    Timestamp                  0
    Open                 1243608
    High                 1243608
    Low                  1243608
    Close                1243608
    Volume_(BTC)         1243608
    Volume_(Currency)    1243608
    Weighted_Price       1243608
    dtype: int64
    
    Empty values (After cleaning) :
    ------------------------------------
    Timestamp            0
    Open                 0
    High                 0
    Low                  0
    Close                0
    Volume_(BTC)         0
    Volume_(Currency)    0
    Weighted_Price       0
    dtype: int64


### #BTC Twitter History [dataset B]
#### Origin_

      URL du dataset_    "https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets/data?select=Bitcoin_tweets.csv"
      
      Oigin file_        "Bitcoin_tweets.csv" 


#### Shape_


```python
df_chunks = pd.read_csv("../input/Bitcoin_tweets.csv", chunksize=100000,lineterminator='\n')
df = pd.concat(df_chunks)
clear_output()

print("------ Bitcoin market historical DataFrame ------\n")
df.info()
```

    ------ Bitcoin market historical DataFrame ------
    
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4689354 entries, 0 to 4689353
    Data columns (total 13 columns):
     #   Column            Dtype 
    ---  ------            ----- 
     0   user_name         object
     1   user_location     object
     2   user_description  object
     3   user_created      object
     4   user_followers    object
     5   user_friends      object
     6   user_favourites   object
     7   user_verified     object
     8   date              object
     9   text              object
     10  hashtags          object
     11  source            object
     12  is_retweet        object
    dtypes: object(13)
    memory usage: 465.1+ MB


#### Content_

    #Variables_ 
                                                             
      * Type "string" (5)   
           - user_name           : The name of the user, as they’ve defined it.
           - user_location	     : The user-defined location for this account’s profile.
           - user_description    : The user-defined UTF-8 string describing their account.
           - text  	             : The actual UTF-8 text of the Tweet
           - hashtags            : All the other hashtags posted in the tweet along with #Bitcoin & #btc

      * Type "numerical" (3)
           - user_followers	     : The number of followers an account currently has.
           - user_friends	     : The number of friends an account currently has.
           - user_favourites     : The number of favorites an account currently has.
        
      * Type "datetime" (2) 
           - user_created        : Time and date, when the account was created.
           - date	             : UTC time and date when the Tweet was created.
        
      * Type "dichotomous" (2)
           - user_verified	     : When true, indicates that the user has a verified account
           - is_retweet          : Indicates whether this Tweet has been Retweeted by the authenticating user

      * Type "categorical" (1)        
           - source	             : Utility used to post the Tweet, Tweets from the Twitter website have a source value - web
        

#### Period_


```python
df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)

start_tweets = df["date"].min()
end_tweets = df["date"].max()
period = end_tweets - start_tweets

print(f"\nstart_market (UTC) : {start_tweets}\nend_market (UTC) : {end_tweets}\nperiod : {period}")

df = df.dropna(subset=['date'])
```

    
    start_market (UTC) : 2021-02-05 10:52:04+00:00
    end_market (UTC) : 2023-01-09 23:59:54+00:00
    period : 703 days 13:07:50


#### Data cleaning_


```python
empty_before = df.isna().sum()
print(f"\nEmpty values (Before cleaning) :\n-------------------------------------\n{empty_before}")

columns_to_fillna = ['user_name', 'user_location', 'user_description', 'hashtags', 'source', 'is_retweet']

for column in columns_to_fillna:
    df[column] = df[column].fillna(f'Uknw_{column}')

empty_after = df.isna().sum()
print(f"\nEmpty values (After cleaning) :\n------------------------------------\n{empty_after}")

tweets_df = df
```

    
    Empty values (Before cleaning) :
    -------------------------------------
    user_name                63
    user_location       2336822
    user_description     519989
    user_created              0
    user_followers            0
    user_friends              0
    user_favourites           0
    user_verified             0
    date                      0
    text                      0
    hashtags              17516
    source                 4066
    is_retweet              752
    dtype: int64
    
    Empty values (After cleaning) :
    ------------------------------------
    user_name           0
    user_location       0
    user_description    0
    user_created        0
    user_followers      0
    user_friends        0
    user_favourites     0
    user_verified       0
    date                0
    text                0
    hashtags            0
    source              0
    is_retweet          0
    dtype: int64


### #Common period_

**Bitcoin_market_historical [A]**

- Start (UTC) : 2011-12-31 07:52:00+00:00   -->     Period : 3377 days, 16:08:00       <--     End (UTC) : 2021-03-31 00:00:00+00:00

**Bitcoin_tweets_historical [B]**

- Start (UTC) : 2021-02-05 10:52:04+00:00   -->     Period : 703 days 13:07:50     <--     End (UTC) : 2023-01-09 23:59:54+00:00


```python
starts = (start_market, start_tweets)
ends = (end_market, end_tweets)

start = max(starts)
end = min(ends)

joint_period = end - start 
print(f"\nThe analysis can start on {str(start)[:10]}, end on {str(end)[:10]}, for a total duration of {joint_period}.\n")
```

    
    The analysis can start on 2021-02-05, end on 2021-03-31, for a total duration of 53 days 13:07:56.
    


### Reduce_



```python
market_df = market_df[(market_df['Timestamp'] >= start) & (market_df['Timestamp'] <= end)]
print("------ Bitcoin market historical DataFrame ------\n")
market_df.info()

tweets_df = tweets_df[(tweets_df['date'] >= start) & (tweets_df['date'] <= end)]
print("\n------ Bitcoin tweets historical DataFrame ------\n")
tweets_df.info()
```

    ------ Bitcoin market historical DataFrame ------
    
    <class 'pandas.core.frame.DataFrame'>
    Index: 76996 entries, 4780269 to 4857376
    Data columns (total 8 columns):
     #   Column             Non-Null Count  Dtype              
    ---  ------             --------------  -----              
     0   Timestamp          76996 non-null  datetime64[ns, UTC]
     1   Open               76996 non-null  float64            
     2   High               76996 non-null  float64            
     3   Low                76996 non-null  float64            
     4   Close              76996 non-null  float64            
     5   Volume_(BTC)       76996 non-null  float64            
     6   Volume_(Currency)  76996 non-null  float64            
     7   Weighted_Price     76996 non-null  float64            
    dtypes: datetime64[ns, UTC](1), float64(7)
    memory usage: 5.3 MB
    
    ------ Bitcoin tweets historical DataFrame ------
    
    <class 'pandas.core.frame.DataFrame'>
    Index: 48583 entries, 0 to 48582
    Data columns (total 13 columns):
     #   Column            Non-Null Count  Dtype              
    ---  ------            --------------  -----              
     0   user_name         48583 non-null  object             
     1   user_location     48583 non-null  object             
     2   user_description  48583 non-null  object             
     3   user_created      48583 non-null  object             
     4   user_followers    48583 non-null  object             
     5   user_friends      48583 non-null  object             
     6   user_favourites   48583 non-null  object             
     7   user_verified     48583 non-null  object             
     8   date              48583 non-null  datetime64[ns, UTC]
     9   text              48583 non-null  object             
     10  hashtags          48583 non-null  object             
     11  source            48583 non-null  object             
     12  is_retweet        48583 non-null  object             
    dtypes: datetime64[ns, UTC](1), object(12)
    memory usage: 5.2+ MB


### Export csv_


```python
market_df.to_csv("../output/Bitcoin_market_historical.csv", index=False )
tweets_df.to_csv("../output/Bitcoin_tweets_historical.csv", index=False)
```

```
(Before) ├── input (2,41Go)
         │   ├── Bitcoin_tweets.csv
         │   └── bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv
         │
 (After) └── output (27,3Mo)
             ├── Bitcoin_market_historical.csv
             └── Bitcoin_tweets_historical.csv
```
