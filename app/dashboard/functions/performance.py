import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np

from sklearn.model_selection import learning_curve

##COLOR##
blue_on_graph = '#1F77B4'
red_on_graph = '#B40426'
background = '#262730'

def plot_correlation_matrix(dataframe): #--------------------------------------------------------------------
    heatmap_params = {
        "annot": True,
        "cmap": 'coolwarm',
        "annot_kws": {"color": "white"}
    }
    title_params = {
        "color": "white",
        "size": 20,
        "loc": 'right'
    }
    tick_params = {
        "axis": 'x',
        "colors": 'white'
    }
    fig_corr, ax_corr = plt.subplots(figsize=(6, 6))         #Création de la figure et de l'axe pour la heatmap
    heatmap = sns.heatmap(dataframe.corr(), ax=ax_corr, **heatmap_params)               #Création de la heatmap
    ax_corr.set_title('Correlation Matrix', **title_params)                             #Configuration du titre

    fig_corr.patch.set_facecolor('None')                                #Configuration de la figure et des axes
    ax_corr.tick_params(**tick_params)
    ax_corr.tick_params(axis='y', colors='white')

    plt.setp(ax_corr.get_xticklabels(), color="white")                   #Configuration des étiquettes des axes
    plt.setp(ax_corr.get_yticklabels(), color="white")

    cbar = heatmap.collections[0].colorbar  # Configuration de la colorbar
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color='white', fontsize=10)

    return fig_corr
def plot_learning_curve(model, X, y, cv=5): #--------------------------------------------------------------------
        train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=cv)      #Apprentissage des courbes
        train_scores_mean = np.mean(train_scores, axis=1)                       #Moyenne des scores d'apprentissage
        test_scores_mean = np.mean(test_scores, axis=1)                   #Moyenne des scores de validation croisée

        plot_params = {                                                         #Configuration des options de style
            "xlabel": ("Training Size", {"color": "white", "size": 5}),
            "ylabel": ("Score", {"color": "white", "size": 5}),
            "title": ("Learning Curve", {"color": "white", "size": 10})
        }
        tick_params = {
            "color": "white",
            "size": 5
        }
        spine_color = 'none'
        legend_params = {
            "fontsize": 5
        }
        grid_params = {
            "color": 'white',
            "linestyle": '-',
            "linewidth": 0.1
        }
        fig_adjust_params = {
            "left": 0.1,
            "right": 0.9,
            "top": 0.9,
            "bottom": 0.1
        }
        fig_learn, ax_learn = plt.subplots(figsize=(3, 2))  #Création de la figure et de l'axe

        ax_learn.plot(train_sizes, train_scores_mean, label="Training score", color='red')  #Tracé de la courbe de score d'apprentissage
        ax_learn.plot(train_sizes, test_scores_mean, label="Cross-validation score", color='blue')  #Tracé de la courbe de score de validation croisée

        ax_learn.set_xlabel(*plot_params["xlabel"])                     #Configuration de l'étiquette de l'axe X
        ax_learn.set_ylabel(*plot_params["ylabel"])                     #Configuration de l'étiquette de l'axe Y
        ax_learn.set_title(*plot_params["title"])                                        #Configuration du titre

        plt.setp(ax_learn.get_xticklabels(), color=tick_params["color"], size=tick_params["size"])  # Configuration des étiquettes de l'axe X
        plt.setp(ax_learn.get_yticklabels(), color=tick_params["color"], size=tick_params["size"])  # Configuration des étiquettes de l'axe Y

        for spine in ax_learn.spines.values():                              #Définir la couleur du cadre (spines)
            spine.set_edgecolor(spine_color)

        ax_learn.set_facecolor('none')                              #Configuration de la couleur de fond de l'axe
        ax_learn.legend(**legend_params)                                                     #Ajout de la légende
        ax_learn.grid(**grid_params)                                                          #Ajout de la grille
        fig_learn.patch.set_facecolor('none')                   #Configuration de la couleur de fond de la figure
        fig_learn.subplots_adjust(**fig_adjust_params)                        #Ajustement des marges de la figure

        return fig_learn

def plot_scatter_real_vs_predicted(y_test, predictions): #--------------------------------------------------------------------
    fig1, ax1 = plt.subplots(figsize=(8, 8))                            #Création de la figure et de l'axe
    ax1.scatter(y_test, predictions)    #Diagramme de dispersion des valeurs prédites par rapport aux valeurs réelles
    ax1.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '-', color='red')            #Ligne de référence
    ax1.set_title('valeurs prédites / valeurs réelles', color='white', fontsize=26, loc='left') #Configuration du titre
    ax1.patch.set_facecolor('none')                                     #Configuration de la couleur de fond de l'axe
    ax1.set_xlabel('Valeurs réelles', color='white', fontsize=22)       #Configuration de l'étiquette de l'axe X
    ax1.set_ylabel('Valeurs prédites', color='white', fontsize=22)      #Configuration de l'étiquette de l'axe Y
    ax1.grid(True, color='gray', linestyle='--', linewidth=0.5)         #Ajout de la grille

    for spine in ax1.spines.values():                                       #Définir la couleur du cadre (spines)
        spine.set_edgecolor('lightgrey')

    plt.setp(ax1.get_xticklabels(), color="white", size='14')           #Configuration des étiquettes de l'axe X
    plt.setp(ax1.get_yticklabels(), color="white", size='14')           #Configuration des étiquettes de l'axe Y

    fig1.patch.set_facecolor('none')                                #Configuration de la couleur de fond de la figure
    fig1.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)  #Ajustement des marges de la figure

    return fig1

def plot_residuals_vs_predicted(y_test, predictions):#--------------------------------------------------------------------
    residuals = y_test - predictions                    #Calcul des résidus
    fig2, ax2 = plt.subplots(figsize=(4, 2))            #Création de la figure et de l'axe

    ax2.scatter(predictions, residuals,
                color='blue')                   #Diagramme de dispersion des résidus par rapport aux valeurs prédites
    ax2.axhline(y=0, color='r', linestyle='-')  #Ligne horizontale à y=0

    ax2.set_xlabel('Valeurs prédites', color='white', fontsize=10)              #Configuration de l'étiquette de l'axe X
    ax2.set_ylabel('Résidus', color='white', fontsize=10)                       #Configuration de l'étiquette de l'axe Y
    ax2.set_title('Residuals Scatterplot vs. Predicted Values', color='white')  #Configuration du titre

    ax2.set_facecolor('#262730')                                    #Configuration de la couleur de fond de l'axe
    fig2.patch.set_facecolor('none')                            #Configuration de la couleur de fond de la figure

    for spine in ax2.spines.values():                                       #Définir la couleur du cadre (spines)
        spine.set_edgecolor('none')

    plt.setp(ax2.get_xticklabels(), color="white", size='5')            #Configuration des étiquettes de l'axe X
    plt.setp(ax2.get_yticklabels(), color="white", size='5')            #Configuration des étiquettes de l'axe Y

    fig2.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)          #Ajustement des marges de la figure

    return fig2

def plot_histogram_of_residuals(residuals):#--------------------------------------------------------------------
    fig3, ax3 = plt.subplots(figsize=(7, 5))            #Création de la figure et de l'axe
    ax3.hist(residuals, bins=30)                        #Histogramme des résidus
    ax3.set_xlabel('Résidus')                           #Configuration de l'étiquette de l'axe X
    ax3.set_ylabel('Fréquence')                         #Configuration de l'étiquette de l'axe Y
    ax3.set_title('Histogramme des résidus')            #Configuration du titre
    return fig3

def plot_density_curve_of_residuals(residuals):#--------------------------------------------------------------------
    fig4, ax4 = plt.subplots(figsize=(5, 4))            #Création de la figure et de l'axe
    sns.kdeplot(residuals, shade=True, ax=ax4)          #Courbe de densité des résidus
    ax4.set_xlabel('Résidus')                           #Configuration de l'étiquette de l'axe X
    ax4.set_ylabel('Densité')                           #Configuration de l'étiquette de l'axe Y
    ax4.set_title('Courbe de densité des résidus')      #Configuration du titre
    return fig4

def plot_qq_diagram(residuals):#------------------------------------------------------------------------------------
    fig5, ax5 = plt.subplots(figsize=(8, 8))
    stats.probplot(residuals, dist="norm", plot=ax5)
    plt.title('Diagramme QQ des résidus', color='white', fontsize=26, loc='left')
    fig5.set_facecolor('none')
    ax5.set_facecolor('none')

    ax5.xaxis.label.set_color('white')
    ax5.xaxis.label.set_fontsize(22)
    ax5.yaxis.label.set_color('white')
    ax5.yaxis.label.set_fontsize(22)

    ax5.tick_params(axis='x', colors='white')  #Couleur rouge pour les graduations de l'axe x
    ax5.tick_params(axis='y', colors='white')  #Couleur bleue pour les graduations de l'axe y

    for spine in ax5.spines.values():
        spine.set_edgecolor('lightgrey')

    ax5.grid(True, color='gray', linestyle='--', linewidth=0.5)

    return fig5

def visualise_performance(model, X, y, y_test, predictions, residuals):

    fig_A = plot_scatter_real_vs_predicted(y_test, predictions)
    fig_B = plot_qq_diagram(residuals)
    fig_C = plot_density_curve_of_residuals(residuals)
    fig_D = plot_histogram_of_residuals(residuals)
    fig_E = plot_correlation_matrix(X)
    fig_F = plot_learning_curve(model, X, y)
    fig_G = plot_residuals_vs_predicted(y_test, predictions)

    col1, col2 = st.columns([5, 4])

    with col1:

        colA, colB = st.columns(2)
        with colA:
            st.pyplot(fig_A)
            st.pyplot(fig_B)
        with colB:
            st.pyplot(fig_C)
            st.pyplot(fig_D)

    with col2:
        st.pyplot(fig_E)
        st.pyplot(fig_F)
        st.pyplot(fig_G)


