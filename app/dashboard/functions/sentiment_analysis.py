from .preprocessing import preprocessing
from .utils import word_chaining_and_count
def text_analysis(tweet_df):
    preprocessed_df = preprocessing(tweet_df)
    occurence_df = word_chaining_and_count(preprocessed_df)
    return preprocessed_df, occurence_df