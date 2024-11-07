import re
import io
from collections import defaultdict
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def shape_wordcloud(df, theme, width=600, height=600, background_color='white', max_words=200, colormap='viridis'):
    """
    Generate a word cloud from the word-frequency pairs in a specific theme column of a DataFrame.

    :param df: The input DataFrame containing the word-frequency data.
    :param theme: The column in the DataFrame that contains word-frequency pairs in the format '[word, count]'.
    :param width: Width of the generated word cloud image.
    :param height: Height of the generated word cloud image.
    :param background_color: Background color of the word cloud.
    :param max_words: Maximum number of words to display in the word cloud.
    :param colormap: Colormap for the word cloud.
    :return: A BytesIO object containing the generated word cloud image.
    """
    word_freq = defaultdict(int)

    for entry in df[theme]:
        if isinstance(entry, str):  # Check if the entry is a string
            pairs = re.findall(r'\[([^,]+), (\d+)\]', entry)  # Extract word-frequency pairs
            for word, freq in pairs:
                try:
                    word_freq[word] += int(freq)  # Add frequency to the word
                except ValueError:
                    continue  # Skip any invalid frequency values
        else:
            continue  # Skip if the entry is not a string

    wordcloud = WordCloud(  # Generate the word cloud
        width=width,
        height=height,
        background_color=background_color,
        max_words=max_words,
        colormap=colormap
    ).generate_from_frequencies(word_freq)

    fig, ax = plt.subplots(figsize=(10, 10), facecolor='white')  # Create a figure to display the word cloud
    ax.imshow(wordcloud, interpolation='bilinear')
    plt.subplots_adjust(left=0.03, right=0.97, top=0.97, bottom=0.03)
    plt.axis('off')

    image_stream = io.BytesIO()  # Save the word cloud image to a BytesIO object
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    plt.close()  # Close the plot to release resources

    return image_stream
