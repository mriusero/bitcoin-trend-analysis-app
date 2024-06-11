import streamlit as st

def page_2(tweet_data):
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">#2 BTC Twitter History [dataset B]</div>', unsafe_allow_html=True)

    st.markdown('<div class="subheader">Description_</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.text("")
        description = """
        
        
        
        Start date (UTC) | 2021-02-05 10:52:04+00:00
        End date   (UTC) | 2021-03-31 00:00:00+00:00
        Period     (UTC) | 53 days 13:07:56    
                    
        [user_name]         -->     le nom de l'utilisateur.
        [user_location]     -->     la localisation définie par l'utilisateur.
        [user_description]  -->     la description du profil de l'utilisateur.
        [user_created]      -->     date et heure de création du compte.
        [user_followers]    -->     le nombre de followers du compte.
        [user_friends]      -->     le nombre d'amis du compte.
        [user_favourites]   -->     le nombre de favoris du compte.
        [user_verified]     -->     (booléen) true indique que l'utilisateur a un compte vérifié.
        [date]              -->     date et heure UTC de l'édition du tweet.
        [text]              -->     le tweet.
        [hashtags]          -->     les hashtags postés dans le tweet.
        [source]            -->     moyen d'édition du tweet.
        [is_retweet]        -->     (booléen) true indique qu'il s'agit d'un retweet.'   
                         """

        st.text(description)
    with col2:
        dataset_info = """
        *             ------ Bitcoin tweets historical DataFrame ------
            
              <class 'pandas.core.frame.DataFrame'>
              Index: 48583 entries, 0 to 48582
              Data columns (total 13 columns):
               #   Column            Non-Null Count  Dtype              
              ---  ------            --------------  -----              
               0   user_name         48583 non-null  object             
               1   user_location     48583 non-null  object             
               2   user_description  48583 non-null  object             
               3   user_created      48583 non-null  object             
               4   user_followers    48583 non-null  object             
               5   user_friends      48583 non-null  object             
               6   user_favourites   48583 non-null  object             
               7   user_verified     48583 non-null  object             
               8   date              48583 non-null  datetime64[ns, UTC]
               9   text              48583 non-null  object             
               10  hashtags          48583 non-null  object             
               11  source            48583 non-null  object             
               12  is_retweet        48583 non-null  object             
              dtypes: datetime64[ns, UTC](1), object(12)
              memory usage: 5.2+ MB
        """
        st.markdown(dataset_info)





    st.dataframe(tweet_data)

    st.markdown('''
        ### Hypotheses

        1. **Analyse de Sentiment sur les Textes des Tweets**

           * **Text** : Utilisez des outils de traitement du langage naturel (NLP) pour déterminer le sentiment (positif, négatif, neutre) des tweets.
           * **Hashtags** : Les hashtags peuvent fournir un contexte supplémentaire au contenu des tweets et influencer le sentiment global. Par exemple, un hashtag comme #Love peut indiquer un sentiment positif.

        2. **Analyse des Utilisateurs**

           * **user_name et user_verified** : Les utilisateurs vérifiés peuvent avoir une influence différente par rapport aux utilisateurs non-vérifiés.
           * **user_location** : Effectuez une analyse géographique pour voir si les sentiments varient selon les régions ou les pays.
           * **user_followers et user_friends** : Ces métriques peuvent indiquer l'influence d'un utilisateur. Analysez si les utilisateurs avec plus de followers expriment des sentiments différents.
           * **user_favourites** : Le nombre de tweets favoris peut également influencer les sentiments, car les utilisateurs ayant plus d'interactions pourraient avoir des tendances spécifiques.

        3. **Analyse Temporelle**

           * **date** : Analyse des tendances, des pics ou des baisses dans les sentiments à des périodes spécifiques.

        4. **Source des Tweets**

           * **source** : Différents clients Twitter (par exemple, Twitter Web App, iPhone, Android) peuvent avoir des utilisateurs avec des comportements différents. Analysez si les sentiments varient en fonction de la source du tweet.

        5. **Interactivité et Viralité**

           * **is_retweet** : Les retweets peuvent avoir des sentiments différents des tweets originaux. Les retweets peuvent souvent amplifier les sentiments présents dans les tweets originaux.
           * Analysez le taux de retweets pour comprendre comment les sentiments se propagent et s'amplifient sur la plateforme.

        6. **Contenu des Profils Utilisateurs**

           * **user_description** : Les descriptions des utilisateurs peuvent fournir un contexte sur leurs intérêts et leur personnalité, ce qui peut influencer le ton et le sentiment de leurs tweets.

        ### Méthodologies

        1. **Traitement du Langage Naturel (NLP)** : Utilisez des bibliothèques comme NLTK, spaCy, ou transformers (BERT, GPT) pour analyser le sentiment des textes.
        2. **Analyse de Clustering** : Groupez les utilisateurs ou les tweets par similitudes de sentiments ou de comportements.
        3. **Visualisation des Données** : Utilisez des outils de visualisation (par ex., Matplotlib, Seaborn) pour créer des graphes temporels des sentiments, des cartes de chaleur géographiques, etc.

        ### Insights Potentiels

        * **Sentiments par Région** : Identifier les régions où les sentiments sont majoritairement positifs ou négatifs.
        * **Impact des Événements** : Observer comment certains événements (par ex., annonces politiques, événements sportifs) influencent le sentiment global sur Twitter.
        * **Profil des Utilisateurs** : Découvrir quels types d'utilisateurs (par ex., influenceurs, nouveaux utilisateurs) sont plus susceptibles d'exprimer des sentiments positifs ou négatifs.
        * **Évolution des Sentiments** : Déterminer comment les sentiments changent au fil du temps et quelles sont les périodes critiques d'évolution.
        ''', unsafe_allow_html=True)
