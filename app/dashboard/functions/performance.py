import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np

from sklearn.model_selection import learning_curve

##COLOR##
blue_on_graph = '#1F77B4'
background = '#262730'
blue_on_graph = '#20edfa'
green_on_graph = '#09AB3B'
red_on_graph = '#d93338'
background = '#1A1C24'
blue_curve= '#3526da'
bitcoin='#ED6F13'
greenmoney="#7DEFA1"
greenlemon="#1bef22"
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
    ax_corr.set_title('', **title_params)                             #Configuration du titre

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
            "xlabel": ("Training Size", {"color": "white", "size": 8}),
            "ylabel": ("Score", {"color": "white", "size": 8}),
            "title": ("", {"color": "white", "size": 10})
        }
        tick_params = {
            "color": "white",
            "size": 7
        }

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

        ax_learn.plot(train_sizes, train_scores_mean, label="Training score", color=red_on_graph)  #Tracé de la courbe de score d'apprentissage
        ax_learn.plot(train_sizes, test_scores_mean, label="Cross-validation score", color=blue_on_graph)  #Tracé de la courbe de score de validation croisée

        ax_learn.set_xlabel(*plot_params["xlabel"])                     #Configuration de l'étiquette de l'axe X
        ax_learn.set_ylabel(*plot_params["ylabel"])                     #Configuration de l'étiquette de l'axe Y
        ax_learn.set_title(*plot_params["title"])                                        #Configuration du titre

        plt.setp(ax_learn.get_xticklabels(), color=tick_params["color"], size=tick_params["size"])  # Configuration des étiquettes de l'axe X
        plt.setp(ax_learn.get_yticklabels(), color=tick_params["color"], size=tick_params["size"])  # Configuration des étiquettes de l'axe Y

        for spine in ax_learn.spines.values():                              #Définir la couleur du cadre (spines)
            spine.set_edgecolor('none')

        ax_learn.set_facecolor('none')                              #Configuration de la couleur de fond de l'axe
        ax_learn.legend(**legend_params)                                                     #Ajout de la légende
        ax_learn.grid(**grid_params)                                                          #Ajout de la grille
        fig_learn.patch.set_facecolor('none')                   #Configuration de la couleur de fond de la figure
        fig_learn.subplots_adjust(**fig_adjust_params)                        #Ajustement des marges de la figure

        return fig_learn

def plot_scatter_real_vs_predicted(y_test, predictions):
    # Create figure and axis
    fig1, ax1 = plt.subplots(figsize=(8, 8))

    # Scatter plot of predicted vs actual values
    ax1.scatter(y_test, predictions, color=blue_on_graph)

    # Reference line
    ax1.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '-', color=red_on_graph)

    # Title configuration
    ax1.set_title('', color='white', fontsize=26, loc='left')

    # Set axis background color
    ax1.patch.set_facecolor('none')

    # X and Y axis labels configuration
    ax1.set_xlabel('Real values', color='white', fontsize=22)
    ax1.set_ylabel('Predicted values', color='white', fontsize=22)

    # Grid configuration
    ax1.grid(True, color='gray', linestyle='--', linewidth=0.5)

    # Spine (frame) color configuration
    for spine in ax1.spines.values():
        spine.set_edgecolor('none')

    # Tick labels configuration
    plt.setp(ax1.get_xticklabels(), color="white", size='14')
    plt.setp(ax1.get_yticklabels(), color="white", size='14')

    # Figure background color and margins adjustment
    fig1.patch.set_facecolor('none')
    fig1.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    return fig1


def plot_residuals_vs_predicted(y_test, predictions):
    # Calculate residuals
    residuals = y_test - predictions

    # Create figure and axis
    fig2, ax2 = plt.subplots(figsize=(4, 2))

    # Scatter plot of residuals vs predicted values
    ax2.scatter(predictions, residuals, color=blue_on_graph)

    # Add horizontal line at y=0
    ax2.axhline(y=0, color='r', linestyle='-')

    # Set labels and title
    ax2.set_xlabel('Predicted values', color='white', fontsize=10)
    ax2.set_ylabel('Residuals', color='white', fontsize=10)
    ax2.set_title('', color='white')

    # Set background color for the axis
    ax2.set_facecolor('#262730')

    # Set facecolor for the figure
    fig2.patch.set_facecolor('none')

    # Remove edge color for all spines
    for spine in ax2.spines.values():
        spine.set_edgecolor('none')

    # Set color and size for x-axis and y-axis tick labels
    plt.setp(ax2.get_xticklabels(), color="white", size='12')
    plt.setp(ax2.get_yticklabels(), color="white", size='12')

    # Adjust figure margins
    fig2.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    return fig2

def plot_histogram_of_residuals(residuals):
    fig3, ax3 = plt.subplots(figsize=(7, 5))  # Création de la figure et de l'axe
    ax3.hist(residuals, bins=30, color=green_on_graph, edgecolor='black', alpha=0.7)  # Histogramme des résidus

    plot_params = {
        "xlabel": ("Residuals", {"color": "white", "size": 10}),
        "ylabel": ("Frequency", {"color": "white", "size": 10}),
        "title": ("", {"color": "white", "size": 12})
    }
    tick_params = {
        "color": "white",
        "size": 12
    }
    grid_params = {
        "color": 'grey',
        "linestyle": '-',
        "linewidth": 0.2
    }
    fig_adjust_params = {
        "left": 0.1,
        "right": 0.9,
        "top": 0.9,
        "bottom": 0.1
    }

    ax3.set_xlabel(*plot_params["xlabel"])  # Configuration de l'étiquette de l'axe X
    ax3.set_ylabel(*plot_params["ylabel"])  # Configuration de l'étiquette de l'axe Y
    ax3.set_title(*plot_params["title"])    # Configuration du titre

    plt.setp(ax3.get_xticklabels(), color=tick_params["color"], size=tick_params["size"])  # Configuration des étiquettes de l'axe X
    plt.setp(ax3.get_yticklabels(), color=tick_params["color"], size=tick_params["size"])  # Configuration des étiquettes de l'axe Y

    ax3.grid(**grid_params)  # Ajout de la grille
    ax3.set_facecolor('none')  # Configuration de la couleur de fond de l'axe

    for spine in ax3.spines.values():  # Définir la couleur du cadre (spines)
        spine.set_edgecolor('none')

    fig3.patch.set_facecolor('none')  # Configuration de la couleur de fond de la figure
    fig3.subplots_adjust(**fig_adjust_params)  # Ajustement des marges de la figure

    return fig3

def plot_density_curve_of_residuals(residuals):
    fig4, ax4 = plt.subplots(figsize=(5, 4))  # Création de la figure et de l'axe
    sns.kdeplot(residuals, shade=True, color=green_on_graph, ax=ax4)  # Courbe de densité des résidus

    plot_params = {
        "xlabel": ("Residuals", {"color": "white", "size": 10}),
        "ylabel": ("Density", {"color": "white", "size": 10}),
        "title": ("", {"color": "white", "size": 12})
    }
    tick_params = {
        "color": "white",
        "size": 8
    }
    grid_params = {
        "color": 'grey',
        "linestyle": '-',
        "linewidth": 0.2
    }
    fig_adjust_params = {
        "left": 0.1,
        "right": 0.9,
        "top": 0.9,
        "bottom": 0.1
    }

    ax4.set_xlabel(*plot_params["xlabel"])  # Configuration de l'étiquette de l'axe X
    ax4.set_ylabel(*plot_params["ylabel"])  # Configuration de l'étiquette de l'axe Y
    ax4.set_title(*plot_params["title"])    # Configuration du titre

    plt.setp(ax4.get_xticklabels(), color=tick_params["color"], size=tick_params["size"])  # Configuration des étiquettes de l'axe X
    plt.setp(ax4.get_yticklabels(), color=tick_params["color"], size=tick_params["size"])  # Configuration des étiquettes de l'axe Y

    ax4.grid(**grid_params)  # Ajout de la grille
    ax4.set_facecolor('none')  # Configuration de la couleur de fond de l'axe

    for spine in ax4.spines.values():  # Définir la couleur du cadre (spines)
        spine.set_edgecolor('none')

    fig4.patch.set_facecolor('none')  # Configuration de la couleur de fond de la figure
    fig4.subplots_adjust(**fig_adjust_params)  # Ajustement des marges de la figure

    return fig4



def plot_qq_diagram(residuals):#------------------------------------------------------------------------------------
    fig5, ax5 = plt.subplots(figsize=(8, 8))
    stats.probplot(residuals, dist="norm", plot=ax5)
    plt.title('', color='white', fontsize=26, loc='left')
    fig5.set_facecolor('none')
    ax5.set_facecolor('none')

    title = ax5.get_title()
    ax5.set_title('', color='white', fontsize=26, loc='left')


    ax5.xaxis.label.set_color('white')
    ax5.xaxis.label.set_fontsize(22)
    ax5.yaxis.label.set_color('white')
    ax5.yaxis.label.set_fontsize(22)

    ax5.tick_params(axis='x', colors='white')  #Couleur rouge pour les graduations de l'axe x
    ax5.tick_params(axis='y', colors='white')  #Couleur bleue pour les graduations de l'axe y

    for spine in ax5.spines.values():
        spine.set_edgecolor('none')

    ax5.grid(True, color='gray', linestyle='--', linewidth=0.5)

    points = ax5.get_lines()[0]
    points.set_marker('o')                  # Définition du marqueur (point)
    points.set_color(blue_on_graph)         # Définition de la couleur des points

    return fig5

def visualise_performance(model, X, y, y_test, predictions, residuals):


    fig_A = plot_scatter_real_vs_predicted(y_test, predictions)
    fig_B = plot_qq_diagram(residuals)
    fig_C = plot_density_curve_of_residuals(residuals)
    fig_D = plot_histogram_of_residuals(residuals)
    fig_E = plot_correlation_matrix(X)
    fig_F = plot_learning_curve(model, X, y)
    fig_G = plot_residuals_vs_predicted(y_test, predictions)

    col1, col2= st.columns([6,9])

    with col1:
        fig_title = ("""
##### # Learning curve_       
    Shows how the model's performance improves with more training data. 
    The x-axis represents the training sample size, and the y-axis shows 
    the model's accuracy or error. It helps in understanding if the model
    would benefit from more data.              
                        """)
        st.markdown(fig_title)
        st.pyplot(fig_F)

        fig_title = ("""
##### # Residuals Scatterplot vs. Predicted Values_
    Displays the difference between predicted and actual values (residuals) 
    on the y-axis against predicted values on the x-axis. It helps assess if
    the model's predictions are consistent across different ranges of values.
                  """)
        st.markdown(fig_title)
        st.pyplot(fig_G)


    with col2:
        fig_title = ("""
##### # Correlation Matrix_
    Visualizes the correlation between different variables in a dataset using colors.
    It helps identify which variables are positively, negatively, or not correlated with each other.
                    """)
        st.markdown(fig_title)
        st.pyplot(fig_E)

    colA, colB = st.columns([15,19])

    with colA:
        fig_title = ("""
##### # Scatter Real vs. Predicted_
    Compares actual values (y-axis) against predicted values (x-axis). 
    It provides a visual representation of how well the model predicts 
    unseen data points.
                """)
        st.markdown(fig_title)
        st.pyplot(fig_A)

        fig_title = ("""
##### # QQ Plot of Residuals_
    Compares the distribution of residuals against a normal distribution. 
    If the points on the plot align closely with the diagonal line, 
    it indicates that residuals are normally distributed.
                """)
        st.markdown(fig_title)
        st.pyplot(fig_B)

    with colB:

        fig_title = ("""
##### # Density curve of residuals_
    Shows the distribution (density) of residuals. It helps assess if 
    residuals follow a particular pattern or distribution, such as normal
    or skewed.
                """)
        st.markdown(fig_title)
        st.pyplot(fig_C)

        fig_title = ("""
##### # Histogram of residuals_
    Displays the frequency distribution of residuals. 
    It provides insights into the spread and shape of residual values.
                """)
        st.markdown(fig_title)
        st.pyplot(fig_D)







