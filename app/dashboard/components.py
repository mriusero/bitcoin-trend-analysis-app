import pandas as pd
import re
import numpy as np
import plotly.graph_objects as go
from matplotlib import pyplot as plt
from scipy.stats import norm

##COLOR##
blue_on_graph = '#1F77B4'
red_on_graph = '#B40426'
background = '#262730'
twitter='#1D9BF0'
bitcoin='#F79621'
primaryColor="#5d38e8"

def gaussian_curve(column_data):
    mu, sigma = norm.fit(column_data)
    xmin, xmax = min(column_data), max(column_data)
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)

    fig, ax = plt.subplots()
    ax.plot(x, p, 'k', linewidth=2, color=red_on_graph)
    ax.hist(column_data, bins=30, density=True, alpha=0.5, color=primaryColor)
    ax.set_title(f'Column {column_data.name}', color="white")
    ax.set_xlabel('Valeurs', color="white")
    ax.set_ylabel('Fréquence', color="white")

    ax.set_facecolor('none')
    fig.patch.set_facecolor('none')

    for spine in ax.spines.values():                                       #Définir la couleur du cadre (spines)
        spine.set_edgecolor('none')

    plt.setp(ax.get_xticklabels(), color="white", size='12')
    plt.setp(ax.get_yticklabels(), color="white", size='12')

    return fig

def volume_curve(df):
    df.reset_index(inplace=True)

    fig_btc, ax1 = plt.subplots(figsize=(10, 6))    # Création de la figure pour le volume en BTC
    ax1.plot(df['Timestamp'], df['Volume_(BTC)'], color='green')    # Tracer la courbe pour le volume en BTC
    ax1.set_xlabel('Temps')
    ax1.set_ylabel('Volume (BTC)', color='green')
    ax1.grid(True)

    ax1_twin = ax1.twinx()      # Ajouter une deuxième courbe pour le prix pondéré (Weighted_Price)
    ax1_twin.plot(df['Timestamp'], df['Weighted_Price'], color='red')
    ax1_twin.set_ylabel('Prix pondéré', color='red')

    ax1.set_facecolor('none')
    fig_btc.patch.set_facecolor('none')

    for spine in ax1.spines.values():  # Définir la couleur du cadre (spines)
        spine.set_edgecolor('none')
    for spine in ax1_twin.spines.values():  # Définir la couleur du cadre (spines)
        spine.set_edgecolor('none')

    plt.setp(ax1.get_xticklabels(), color="white", size='12')
    plt.setp(ax1.get_yticklabels(), color="white", size='12')
    plt.setp(ax1_twin.get_xticklabels(), color="white", size='12')
    plt.setp(ax1_twin.get_yticklabels(), color="white", size='12')

    fig_currency, ax2 = plt.subplots(figsize=(10, 6))   # Création de la figure pour le volume en Currency
    ax2.plot(df['Timestamp'], df['Volume_(Currency)'], color='blue')    # Tracer la courbe pour le volume en Currency
    ax2.set_xlabel('Temps')
    ax2.set_ylabel('Volume (Currency)', color='blue')
    ax2.grid(True)

    ax2_twin = ax2.twinx()      # Ajouter une deuxième courbe pour le prix pondéré (Weighted_Price)
    ax2_twin.plot(df['Timestamp'], df['Weighted_Price'], color='red')
    ax2_twin.set_ylabel('Prix pondéré', color='red')

    ax2.set_facecolor('none')
    ax2_twin.set_facecolor('none')
    fig_currency.patch.set_facecolor('none')
    for spine in ax2.spines.values():  # Définir la couleur du cadre (spines)
        spine.set_edgecolor('none')
    for spine in ax2_twin.spines.values():  # Définir la couleur du cadre (spines)
        spine.set_edgecolor('none')
    plt.setp(ax2.get_xticklabels(), color="white", size='12')
    plt.setp(ax2.get_yticklabels(), color="white", size='12')
    plt.setp(ax2_twin.get_xticklabels(), color="white", size='12')
    plt.setp(ax2_twin.get_yticklabels(), color="white", size='12')
    grid_params = {
        "color": 'none',
        "linestyle": '-',
        "linewidth": 0.1
    }
    ax1.grid(**grid_params)
    ax1_twin.grid(**grid_params)
    ax2.grid(**grid_params)
    ax2_twin.grid(**grid_params)



    return fig_btc, fig_currency





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
                             line = dict(color=primaryColor)
                             )
                  )
    fig.update_layout(title="",
                      xaxis_title="Date",
                      yaxis_title="Price",
                      xaxis_rangeslider_visible=False)

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
