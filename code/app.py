import streamlit as st
from pagina_inicial import pagina_inicial
from sumarizacao_frequencia import sumarizacao_frequencia

import streamlit as st
import re
import nltk
import string
import pandas as pd
import unicodedata
import heapq
import math
import nltk
nltk.download('stopwords')

def main():
   # st.sidebar.title('Menu')

    # Definindo o menu lateral
    pagina_selecionada = st.sidebar.radio('Menu', [  'Sumarização de Frequência'])
 

    # Verificando a página selecionada e chamando a função correspondente
    if pagina_selecionada == 'Sumarização de Frequência':
        sumarizacao_frequencia()
 

if __name__ == "__main__":
    main()

