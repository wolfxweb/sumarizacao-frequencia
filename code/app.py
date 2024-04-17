import streamlit as st
from pagina_inicial import pagina_inicial
from sumarizacao_frequencia import sumarizacao_frequencia

import re
import nltk
import string
import heapq
from goose3 import Goose
import spacy

def main():
   # st.sidebar.title('Menu')

    # Definindo o menu lateral
    pagina_selecionada = st.sidebar.radio('Menu', [  'Página Inicial', 'Sumarização de Frequência'])
 

    # Verificando a página selecionada e chamando a função correspondente
    if pagina_selecionada == 'Página Inicial':
        pagina_inicial()
    elif pagina_selecionada == 'Sumarização de Frequência':
        sumarizacao_frequencia()
 

if __name__ == "__main__":
    main()

