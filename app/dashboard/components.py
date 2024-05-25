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
    # Filtrer les mots avec un Count > 1
    df_filtered = df[df['count'] > 1]

    # Trier le DataFrame par ordre décroissant des comptes
    df_sorted = df_filtered.sort_values(by='count', ascending=False)

    # Calculer les pourcentages cumulés
    df_sorted['cumulative_percentage'] = df_sorted['count'].cumsum() / df_sorted['count'].sum() * 100

    # Tracer le graphique de Pareto
    fig, ax1 = plt.subplots()

    ax1.bar(df_sorted['word'], df_sorted['count'], color='b')
    ax1.set_xlabel('Mots')
    ax1.set_ylabel('Comptes', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(df_sorted['word'], df_sorted['cumulative_percentage'], color='r', marker='o', linestyle='-')
    ax2.set_ylabel('Pourcentage cumulatif', color='r')
    ax2.tick_params('y', colors='r')

    plt.title('Graphique de Pareto')
    plt.xticks(rotation=90)
    plt.tight_layout()

    return fig



