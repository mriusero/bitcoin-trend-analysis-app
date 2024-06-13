# Phase 1 : Data Exploration

## (1) Import des librairies


```python
import pandas as pd
from datetime import datetime, timezone
from IPython.display import clear_output
import gc
```

## (2) Dataset Exploration
### (2.1) Dataset 1 : Bitcoin Historical Data
#### (2.1.1) Description 

- **data origin** : https://www.kaggle.com

- **URL du dataset** : https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data

- **origin file** : "bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv" 

- **Shape** : ( 8 Columns ; 4857377 Entries)

- **Variables** :  

  * int64 = (1)  
      * Timestamp : *Start time of time window (60s window), in Unix time*
                                                          
  * object = (7)   
      * Open : *Open price at start time window*
      * High : *High price within time window*               
      * Low : *Low price within time window*              
      * Close : *Close price at end of time window*            
      * Volume_(BTC) : *Volume of BTC transacted in this window*      
      * Volume_(Currency) : *Volume of corresponding currency transacted in this window* 
      * Weighted_Price : VWAP *Volume Weighted Average Price*     


```python
df = pd.read_csv("../input/bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv")
print("------ Bitcoin market historical DataFrame ------\n")
df.info()
df.head(5) 
```

    ------ Bitcoin market historical DataFrame ------
    
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





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Timestamp</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume_(BTC)</th>
      <th>Volume_(Currency)</th>
      <th>Weighted_Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1325317920</td>
      <td>4.39</td>
      <td>4.39</td>
      <td>4.39</td>
      <td>4.39</td>
      <td>0.455581</td>
      <td>2.0</td>
      <td>4.39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1325317980</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1325318040</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1325318100</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1325318160</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### (2.1.2) Data cleaning
**(a)** Time analysis
- "Timestamp" column datetime casted with UTC 
- Measurment period identification


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


**(b)** Drop NA 
- EMPTY VALUES -> From 4 857 377 to 3 613 769 entries = *1 243 608 empty entries deleted* 


```python
empty = df.isna().sum()
print(f"--> Empty values (before cleaning) :\n\n{empty}")

df = df.dropna()

empty = df.isna().sum()
print(f"\n--> Empty_values (after cleaning) :\n\n{empty}\n")

market_df = df.copy()

```

    --> Empty values (before cleaning) :
    
    Timestamp                  0
    Open                 1243608
    High                 1243608
    Low                  1243608
    Close                1243608
    Volume_(BTC)         1243608
    Volume_(Currency)    1243608
    Weighted_Price       1243608
    dtype: int64
    
    --> Empty_values (after cleaning) :
    
    Timestamp            0
    Open                 0
    High                 0
    Low                  0
    Close                0
    Volume_(BTC)         0
    Volume_(Currency)    0
    Weighted_Price       0
    dtype: int64
    


### (2.2) Dataset 2 : Bitcoin Historical Tweets
#### (2.2.1) Description 

- **data origin** : https://www.kaggle.com

- **URL du dataset** : https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets/data?select=Bitcoin_tweets.csv

- **origin file** : "Bitcoin_tweets.csv" 

- **Shape** : ( 13 Columns ; 4 689 354 Entries)

- **Variables** :  
                                                         
  * object = (13)   
    - user_name	         : *The name of the user, as they’ve defined it.*
    - user_location	     : *The user-defined location for this account’s profile.*
    - user_description   : *The user-defined UTF-8 string describing their account.*
    - user_created       : *Time and date, when the account was created.*
    - user_followers	   : *The number of followers an account currently has.*
    - user_friends	     : *The number of friends an account currently has.*
    - user_favourites	   : *The number of favorites an account currently has*
    - user_verified	     : *When true, indicates that the user has a verified account*
    - date	             : *UTC time and date when the Tweet was created*
    - text  	           : *The actual UTF-8 text of the Tweet*
    - hashtags	         : *All the other hashtags posted in the tweet along with #Bitcoin & #btc*
    - source	           : *Utility used to post the Tweet, Tweets from the Twitter website have a source value - web*
    - is_retweet	       : *Indicates whether this Tweet has been Retweeted by the authenticating user.*


```python
df_chunks = pd.read_csv("../input/Bitcoin_tweets.csv", chunksize=100000,lineterminator='\n')
df = pd.concat(df_chunks)

clear_output()
print("------ Bitcoin market historical DataFrame ------\n")
df.info()
df.head(5)
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





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_name</th>
      <th>user_location</th>
      <th>user_description</th>
      <th>user_created</th>
      <th>user_followers</th>
      <th>user_friends</th>
      <th>user_favourites</th>
      <th>user_verified</th>
      <th>date</th>
      <th>text</th>
      <th>hashtags</th>
      <th>source</th>
      <th>is_retweet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DeSota Wilson</td>
      <td>Atlanta, GA</td>
      <td>Biz Consultant, real estate, fintech, startups...</td>
      <td>2009-04-26 20:05:09</td>
      <td>8534.0</td>
      <td>7605</td>
      <td>4838</td>
      <td>False</td>
      <td>2021-02-10 23:59:04</td>
      <td>Blue Ridge Bank shares halted by NYSE after #b...</td>
      <td>['bitcoin']</td>
      <td>Twitter Web App</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CryptoND</td>
      <td>NaN</td>
      <td>😎 BITCOINLIVE is a Dutch platform aimed at inf...</td>
      <td>2019-10-17 20:12:10</td>
      <td>6769.0</td>
      <td>1532</td>
      <td>25483</td>
      <td>False</td>
      <td>2021-02-10 23:58:48</td>
      <td>😎 Today, that's this #Thursday, we will do a "...</td>
      <td>['Thursday', 'Btc', 'wallet', 'security']</td>
      <td>Twitter for Android</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tdlmatias</td>
      <td>London, England</td>
      <td>IM Academy : The best #forex, #SelfEducation, ...</td>
      <td>2014-11-10 10:50:37</td>
      <td>128.0</td>
      <td>332</td>
      <td>924</td>
      <td>False</td>
      <td>2021-02-10 23:54:48</td>
      <td>Guys evening, I have read this article about B...</td>
      <td>NaN</td>
      <td>Twitter Web App</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Crypto is the future</td>
      <td>NaN</td>
      <td>I will post a lot of buying signals for BTC tr...</td>
      <td>2019-09-28 16:48:12</td>
      <td>625.0</td>
      <td>129</td>
      <td>14</td>
      <td>False</td>
      <td>2021-02-10 23:54:33</td>
      <td>$BTC A big chance in a billion! Price: \487264...</td>
      <td>['Bitcoin', 'FX', 'BTC', 'crypto']</td>
      <td>dlvr.it</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alex Kirchmaier 🇦🇹🇸🇪 #FactsSuperspreader</td>
      <td>Europa</td>
      <td>Co-founder @RENJERJerky | Forbes 30Under30 | I...</td>
      <td>2016-02-03 13:15:55</td>
      <td>1249.0</td>
      <td>1472</td>
      <td>10482</td>
      <td>False</td>
      <td>2021-02-10 23:54:06</td>
      <td>This network is secured by 9 508 nodes as of t...</td>
      <td>['BTC']</td>
      <td>Twitter Web App</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



#### (2.1.3) Nettoyage des données

**(a)** Dans l'objectif d'analyser la corrélation entre le corps de texte d'un tweet et le cours du BTC, seul les champs "date" et "texte" sont essentiels à 100% :

- date -> *conversion en type datetime + suppression des dates nulles (66 entries)*


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


**(b)** Pour les catégories qui contiennent des valeurs nulles, définition d'une key value avec le préfiwe 'Uknw' : 

- user_name, user_location, user_description, hashtags, source, is_retweet -> *unkown category key definition*


```python
empty = df.isna().sum()
print(f"--> Empty_values (before cleaning) :\n\n{empty}")

columns_to_fillna = ['user_name', 'user_location', 'user_description', 'hashtags', 'source', 'is_retweet']

for column in columns_to_fillna:
    df[column] = df[column].fillna(f'Uknw_{column}')

empty = df.isna().sum()
print(f"--> Empty_values (after cleaning) :\n\n{empty}")

tweets_df = df
```

    --> Empty_values (before cleaning) :
    
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
    --> Empty_values (after cleaning) :
    
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


### (2.3) Filtrage des données sur la période

#### (2.3.1) Identification de la période

**Bitcoin_market_historical**

- Date de début (UTC) : 2011-12-31 07:52:00+00:00   -->     Période : 3377 days, 16:08:00       <--     Date de fin (UTC) : 2021-03-31 00:00:00+00:00

**Bitcoin_tweets_historical**

- Date de début (UTC) : 2021-02-05 10:52:04+00:00   -->     Période : 703 days 13:07:50     <--     Date de fin (UTC) : 2023-01-09 23:59:54+00:00


```python
starts = (start_market, start_tweets)
ends = (end_market, end_tweets)

start = max(starts)
end = min(ends)

joint_period = end - start 

print(f"L'analyse peut démarrer le {str(start)[:10]} et se terminer le {str(end)[:10]}, soit une période d'analyse de {joint_period}")
```

    L'analyse peut démarrer le 2021-02-05 et se terminer le 2021-03-31, soit une période d'analyse de 53 days 13:07:56


#### (2.3.2) Filtrage 


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


### (2.4) Export csv


```python
market_df.to_csv("../output/Bitcoin_market_historical.csv", index=False )
tweets_df.to_csv("../output/Bitcoin_tweets_historical.csv", index=False)
```

```
├── input (2,41Go)
│   ├── Bitcoin_tweets.csv
│   └── bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv
└── output (27,3Mo)
    ├── Bitcoin_market_historical.csv
    └── Bitcoin_tweets_historical.csv
```

## (3) Libération mémoire


```python
del  column, columns_to_fillna, df, df_chunks, empty, end, ends, end_market, end_tweets, joint_period, market_df, period, start_market, start_tweets, start, starts, tweets_df
gc.collect()
```




    0


