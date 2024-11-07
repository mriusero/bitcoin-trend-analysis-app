# Bitcoin Trend Analysis App

This repository contains a Streamlit application for visualizing and analyzing trends related to Bitcoin tweets and market data. Developed within a learning context, this project focuses on data management, visualization, and text mining.

## Project Overview

The project is organized into three main phases:

### 1. Data Management

Data preprocessing and analysis are conducted using Jupyter Notebooks with Pandas to prepare two key datasets:

- **Bitcoin Market History:** Analysis and cleaning of historical market data.
- **Bitcoin Twitter History:** Analysis and cleaning of tweet data related to Bitcoin.
- **Cross-Referencing Time Periods:** Identifying overlapping time periods between datasets and exporting dataframes for further analysis.

### 2. Data Visualization

Data visualization and additional preprocessing are performed on both datasets:

- **Preprocessing:** Utilizes NLTK tools (e.g., SnowballStemmer, stopwords) to process text.
- **Feature Engineering:** Adds new variables for analysis, such as sentiment scores using VaderSentiment, time-series aggregation, and word clouds.
- **Visualization & Trend Analysis:** Includes trend visualization and statistical calculations using Numpy, Scipy, and Matplotlib.

### 3. Correlation and Predictive Analysis

A correlation study between 'Bitcoin Market History' and 'Bitcoin Twitter History' is performed, with a predictive model for trend analysis:

- **Modular Linear Regression Model:** Built using Scikit-Learn and Streamlit widgets for interactive exploration.
- **Market Prediction Comparison:** Visualized with Dash Plotly to compare model predictions against market data.
- **Prediction Performance Visualization:** Detailed performance metrics and visualizations using Numpy, Scipy, Matplotlib, and Seaborn.

## Project Structure

```plaintext
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
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/mriusero/projet-sda-dash-streamlit.git
cd projet-sda-dash-streamlit
```

### Create and Activate Virtual Environment (Recommended)

#### On macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

To start the Streamlit application, run the following from the root directory:

```bash
cd app 
streamlit run app/app.py
```

## Key Files and Directories

- **app.py:** The main entry point for launching the Streamlit application.
- **dashboard/:** Houses components, layout, and page content for the dashboard.
- **data/:** Contains raw data, exploratory notebooks, and preprocessed outputs.

## Data Directory Structure

```plaintext
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
```

### Exploration
- **dataset_exploration.ipynb:** Jupyter notebook for exploratory data analysis (EDA) of the datasets.
- **dataset_exploration.md:** Markdown summary of findings from the EDA notebook.

### Input
- **Bitcoin_tweets.csv:** Raw tweet data related to Bitcoin, including text, timestamps, and metadata.
- **bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv:** Historical Bitcoin market data at one-minute intervals, including price and volume.

### Output
- **Bitcoin_market_historical.csv:** Cleaned and processed Bitcoin market data for analysis.
- **Bitcoin_tweets_historical.csv:** Cleaned and processed tweet data for sentiment analysis and trend detection.

### Sentiment
- **preprocessed_data.csv:** Tokenized text data ready for sentiment analysis.
- **sentiment_analysis.csv:** Results of the sentiment analysis, including sentiment scores and categorized sentiments.

## License

This project is open-source and can be freely used and modified under the [MIT License](LICENSE).
