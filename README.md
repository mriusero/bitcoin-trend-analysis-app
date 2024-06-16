# projet-sda-dash-streamlit
This repository contains a Streamlit application designed for visualizing and analyzing data related to Bitcoin tweets and market trends. This project is undertaken within the Sorbonne Data Analytics learning context, focusing on data management, data visualization, and text mining.

  (1) The first step is the Data Management phase, carried out on jupyter_notebook with Pandas : 

    - Analysis and cleaning of the first dataset : Bitcoin Market History 
    - Analysis and cleaning of the second dataset : Bitcoin Twitter History
    - Cross time period identification and dataframe export for analysis

  (2) The second step is the Data Visualisation phase, carried out on both dataframes :

    - Preprocessing with nltk (SnowballStemmer, Stopwords) 
    - Adding value through new variables creation (Sentiment analysis with VaderSentiment, Times series aggregation, Wordcloud ...)             
    - Statistics calculation and trends visualisation with Numpy, Scipy, Matplotlib 

  (3) Analytics study of correlation between 'Bitcoin Market History' & 'Bitcoin Twitter History':

    - Modular Linear Regression Model creation with sklearn and streamlit widgets
    - Prediction comparison to market with Dash Plotly 
    - Prediction performance vizualisation with Numpy, Scipy, Matplotlib, Seaborn


## Project Structure
    projet-sda-dash-streamlit
    ├── README.md
    ├── app
    │   ├── app.py
    │   ├── dashboard
    │   │   ├── __init__.py
    │   │   ├── components.py
    │   │   ├── content
    │   │   │   ├── __init__.py
    │   │   │   ├── page0.py
    │   │   │   ├── page1.py
    │   │   │   ├── page2.py
    │   │   │   ├── page3.py
    │   │   │   ├── pageconclu.py
    │   │   │   └── pageintro.py
    │   │   ├── functions
    │   │   │   ├── __init__.py
    │   │   │   ├── model.py
    │   │   │   ├── performance.py
    │   │   │   ├── preprocessing.py
    │   │   │   ├── sentiment_analysis.py
    │   │   │   ├── utils.py
    │   │   │   └── wordcloud.py
    │   │   ├── layout.py
    │   │   └── styles.css
    │   └── data
    │       ├── exploration
    │       │   ├── dataset_exploration.ipynb
    │       │   └── dataset_exploration.md
    │       ├── input
    │       │   ├── Bitcoin_tweets.csv
    │       │   └── bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv
    │       ├── output
    │       │   ├── Bitcoin_market_historical.csv
    │       │   └── Bitcoin_tweets_historical.csv
    │       └── sentiment
    │           ├── preprocessed_data.csv
    │           └── sentiment_analysis.csv
    └── requirements.txt


## Installation

### Prerequisites
- Python 3.8 or higher 
- pip (Python package installer)

### Clone the Repository
    git clone https://github.com/yourusername/projet-sda-dash-streamlit.git
    cd projet-sda-dash-streamlit

## Create and Activate Virtual Environment (Optional but Recommended)

### On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

### On Windows
    python -m venv venv
    venv\Scripts\activate

## Install Dependencies
    pip install -r requirements.txt

## Running the Application
To start the Streamlit application, run the following command from the root directory of the project:
    
    streamlit run app/app.py

## Project Details

- **app.py:** The main entry point of the Streamlit application.
- **dashboard/:** Contains the components, layout, and content for the dashboard.
- **data/:** Contains the input data files, exploratory notebooks, and preprocessed data outputs. 

## Data Directory Structure
    data
    ├── exploration
    │   ├── dataset_exploration.ipynb
    │   └── dataset_exploration.md
    ├── input
    │   ├── Bitcoin_tweets.csv
    │   └── bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv
    ├── output
    │   ├── Bitcoin_market_historical.csv
    │   └── Bitcoin_tweets_historical.csv
    └── sentiment
        ├── preprocessed_data.csv
        └── sentiment_analysis.csv

### Exploration
- **dataset_exploration.ipynb:** A Jupyter notebook containing exploratory data analysis (EDA) of the datasets.
- **dataset_exploration.md:** A markdown file summarizing the findings from the EDA notebook.

### Input
- **Bitcoin_tweets.csv:** This dataset contains raw tweet data related to Bitcoin. It includes tweet texts, timestamps, user information, and other relevant metadata.
- **bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv:** This dataset contains historical Bitcoin market data with one-minute intervals. It includes open, high, low, close prices, and trading volume.

### Output
- **Bitcoin_market_historical.csv:** This dataset contains processed and cleaned Bitcoin market data, derived from the input dataset, used for further analysis and visualization.
- **Bitcoin_tweets_historical.csv:** This dataset contains processed and cleaned tweet data, derived from the input dataset, used for sentiment analysis and trend detection.

### Sentiment
- **preprocessed_data.csv:** This dataset contains preprocessed data used for sentiment analysis. It includes cleaned and tokenized text data ready for sentiment scoring.
- **sentiment_analysis.csv:** This dataset contains the results of the sentiment analysis performed on the preprocessed tweet data. It includes sentiment scores, categorized sentiments (positive, negative, neutral), and other relevant features.

## Personnal notes
- Start: 2024-05-06
- End: 024-06-16 

## License
This project is licensed under the MIT License. See the LICENSE file for more details.