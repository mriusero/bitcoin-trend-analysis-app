import pandas as pd
import plotly.graph_objects as go
from matplotlib import pyplot as plt

def create_candlestick_chart1(df):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df["Open"],
                                         high=df["High"],
                                         low=df["Low"],
                                         close=df["Close"]
                                         )
                          ]
                    )
    return fig

def create_candlestick_chart2(df):
    fig = go.Figure(data=[go.Candlestick(x=df['date'],
                                         open=df["Open"],
                                         high=df["High"],
                                         low=df["Low"],
                                         close=df["Close"]
                                         )
                          ]
    )
    # Ajout de la courbe des prédictions
    fig.add_trace(go.Scatter(x=df['date'],
                             y=df['prediction'],
                             mode='lines',
                             name='Prediction',
                             line=dict(color='blue', width=2)
                             )
    )

    # Mise en forme du graphique
    fig.update_layout(
                      title='',
                      height=500,
                      #width=100,
                      xaxis_rangeslider_visible=False,
    )
    return fig


def create_circular_graph(df):
    # Trier le DataFrame par ordre décroissant des comptes
    df_sorted = df.sort_values(by='count', ascending=False)

    # Calculer les pourcentages des comptes
    df_sorted['percentage'] = df_sorted['count'] / df_sorted['count'].sum() * 100

    # Calculer les pourcentages cumulés
    df_sorted['cumulative_percentage'] = df_sorted['percentage'].cumsum()

    # Filtrer les mots pour obtenir ceux qui représentent les 20% les plus utilisés
    df_filtered = df_sorted[df_sorted['cumulative_percentage'] <= 20]

    # Tracer le graphique circulaire
    fig, ax = plt.subplots()
    ax.pie(df_filtered['percentage'], labels=df_filtered['word'], autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Graphique Circulaire des 20% des Mots les Plus Utilisés')
    plt.tight_layout()

    return fig



