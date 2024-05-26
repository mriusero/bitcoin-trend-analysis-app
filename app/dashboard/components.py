import plotly.graph_objects as go
from matplotlib import pyplot as plt


def create_candlestick_chart(df):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df["Open"],
                                         high=df["High"],
                                         low=df["Low"],
                                         close=df["Close"]
                                         )
                          ]
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



