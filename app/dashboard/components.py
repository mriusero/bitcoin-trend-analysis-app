import numpy as np
import plotly.graph_objects as go
from matplotlib import pyplot as plt
from scipy.stats import norm

##COLOR##
blue_on_graph = '#20edfa'
green_on_graph = '#09AB3B'
red_on_graph = '#d93338'
background = '#262730'
blue_curve= '#3526da'
bitcoin='#ED6F13'
greenmoney="#7DEFA1"
greenlemon="#1bef22"

def gaussian_curve(column_data):
    mu, sigma = norm.fit(column_data)
    xmin, xmax = min(column_data), max(column_data)
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, p, linewidth=4, color=green_on_graph, label='Gaussian Curve')
    ax.hist(column_data, bins=30, density=True, alpha=0.5, color=blue_on_graph)
    ax.set_title(f'{column_data.name}_', color="white", size=20, loc='right')

    ax.yaxis.set_label_position('right')
    ax.yaxis.tick_right()

    ax.set_facecolor('none')
    fig.patch.set_facecolor('none')

    for spine in ax.spines.values():
        spine.set_edgecolor('none')

    ax.tick_params(axis='x', which='both', color='white')
    ax.tick_params(axis='y', which='both', color='white')

    plt.setp(ax.get_xticklabels(), color="white", size='12')
    plt.setp(ax.get_yticklabels(), color="white", size='12')

    return fig

def combined_volume_curve(df):
    df['date'] = df.index.strftime('%y-%m-%d')
    fig, ax1 = plt.subplots(figsize=(12, 8))

    ax1.bar(df['date'], df['Volume_(BTC)'], color=blue_on_graph, label='Volume (BTC)', alpha=0.6) # Etape 1: Histogramme pour le volume en BTC
    ax1.set_xlabel('Time', color='white', size=15)
    ax1.set_ylabel('Volume (BTC)', color='white', size=15)
    ax1.tick_params(axis='y', labelcolor=blue_on_graph)
    ax1.xaxis.set_tick_params(color='none')
    ax1.yaxis.set_tick_params(color='white')
    ax1.set_facecolor('none')

    ax2 = ax1.twinx()       # Etape 2: Histogramme pour le volume en Currency
    ax2.bar(df['date'], df['Volume_(Currency)'], color=red_on_graph, label='Volume (Currency)', alpha=0.6, width=0.4)
    ax2.set_ylabel('Volume (Currency)', color='white', size=15)
    ax2.tick_params(axis='y', labelcolor='white')
    ax2.yaxis.set_tick_params(color='white')
    ax2.set_facecolor('none')

    ax3 = ax1.twinx()   # Etape 3: Courbe pour le prix pondéré
    ax3.plot(df['date'], df['Weighted_Price'], color=green_on_graph, label='Weighted Price',  linewidth=2)
    ax3.spines['right'].set_position(('outward', 60))           # Décaler l'axe pour le différencier
    ax3.set_ylabel('Weighted_price', color='white', size=15)
    ax3.tick_params(axis='y', labelcolor=green_on_graph)
    ax3.yaxis.set_tick_params(color=green_on_graph)
    ax3.set_facecolor('none')

    for ax in [ax1, ax2, ax3]:      # Configuration des ticks et des spines pour tous les axes
        ax.tick_params(axis='x', which='both', labelbottom=False)
        ax.spines['left'].set_edgecolor("#4b4b4b")
        ax.spines['right'].set_edgecolor("#4b4b4b")
        ax.spines['top'].set_edgecolor("none")
        ax.spines['bottom'].set_edgecolor("none")

    ax3.spines['right'].set_edgecolor(green_on_graph)

    fig.patch.set_facecolor('none')

    for ax in [ax1, ax2, ax3]:      # Configuration des labels de ticks
        plt.setp(ax.get_xticklabels(), color="white", size='14')
        plt.setp(ax.get_yticklabels(), color="white", size='14')

    grid_params = {          # Configuration de la grille
        "color": 'none',
        "linestyle": '-',
        "linewidth": 0.1
    }
    ax1.grid(**grid_params)
    ax2.grid(**grid_params)
    ax3.grid(**grid_params)

    legend = fig.legend(loc='upper left', bbox_to_anchor=(0.75, 1.1), bbox_transform=ax1.transAxes)
    legend.set_frame_on(True)
    legend.get_frame().set_facecolor('none')
    for text in legend.get_texts():
        text.set_color('white')

    return fig


def create_candlestick_chart1(df):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df.index,
                                 open=df["Open"],
                                 high=df["High"],
                                 low=df["Low"],
                                 close=df["Close"],
                                 )
                  )
    fig.add_trace(go.Scatter(x=df.index,
                             y=df['Weighted_Price'],
                             mode="lines",
                             name="Weighted_Price",
                             line = dict(color=blue_curve)
                             )
                  )
    fig.update_layout(title="",
                      xaxis_title="Date",
                      yaxis_title="Price",
                      xaxis_rangeslider_visible=False,
                      margin = dict(l=50, r=50, t=20, b=50),
                      xaxis = dict(
                          tickfont=dict(size=15)  # Ajustez la taille de la police pour l'axe x
                      ),
                      yaxis = dict(
                          tickfont=dict(size=15)  # Ajustez la taille de la police pour l'axe y
                      )
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
                             line=dict(color=blue_curve, width=2)
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

