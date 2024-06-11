import streamlit as st

def page_0():
    st.markdown('<div class="title">SDA_2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="header"># Introduction_</div>', unsafe_allow_html=True)

    st.markdown("")
    introduction = """

    Bitcoin (₿) est une cryptomonnaie inventée en 2008 par une personne ou un groupe de personnes inconnues,
    utilisant le nom de Satoshi Nakamoto et dont l'utilisation à démarré en 2009 lorsque son implémentation 
    a été publiée en tant que logiciel libre.

    Bitcoin est une monnaie numérique décentralisée, sans banque centrale ni administrateur unique, qui peut être
    envoyée d'utilisateur à utilisateur sur le réseau bitcoin peer-to-peer sans besoin d'intermédiaires.  
    Les transactions sont vérifiées par les nœuds du réseau grâce à la cryptographie et enregistrées dans un registre
    distribué public, appelé blockchain. 

    Le 30 novembre 2020, le bitcoin a atteint un nouveau record historique de 19 860 $, dépassant le précédent record de décembre 2017.
    Le 19 janvier 2021, Elon Musk a placé #Bitcoin dans son profil Twitter en tweetant "Avec le recul, c'était inévitable", 
    ce qui a provoqué une hausse du prix de près de 5000 $ en une heure pour atteindre 37 299 $.
        """
    st.text(introduction)

    st.markdown('<div class="header"># Targets_</div>', unsafe_allow_html=True)