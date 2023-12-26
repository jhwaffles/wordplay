import os, sys
PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(PACKAGE_DIR)

import streamlit as st
from gensim.models import KeyedVectors
import gensim.downloader as api
import pandas as pd


@st.cache(allow_output_mutation=True)
def load_model(model_name):
    word2vec = api.load(model_name)
    return word2vec


def main():
    """
        WordPlay - Gensim Playground
    """
    activity = ["Word2Vec Playground"]
    choice = st.sidebar.selectbox("Choose Activity",activity)
    
    #GENSIM
    if choice == "Word2Vec Playground":
        
        models = {
            "Wiki - 6B Tokens, 50 Dimensions": "glove-wiki-gigaword-50",
            "Twitter - 2B Tokens, 50 Dimensions": "glove-twitter-50"
        }
            
        model_key = st.selectbox("Choose Model", list(models.keys()))
        
        word2vec = load_model(models[model_key])
        
        word = st.text_input("Enter Word")
        topn = st.number_input("Top N Closest words", 1, 100)
        if word and topn:
            output = word2vec.similar_by_word(word.lower(),topn=topn)
            st.dataframe(pd.DataFrame(output, columns=["Word", "Score"]))
            
        st.subheader("If A-->B, then C-->?? Example: Man --> King, then Woman --> Queen")
        wordA = st.text_input("A")
        wordB = st.text_input("B")
        wordC = st.text_input("C")
        if wordA and wordB and wordC:
            output = word2vec.most_similar_cosmul(positive=[wordB.lower(), wordC.lower()], negative=[wordA.lower()])
            st.dataframe(pd.DataFrame(output, columns=["Word", "Score"]))
        
    
if __name__ == "__main__":
    main()