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

def remove_acentuacao(texto):
    # Remove a acentuação usando a biblioteca unicodedata
    return ''.join(caracter for caracter in unicodedata.normalize('NFD', texto) if unicodedata.category(caracter) != 'Mn')

def processaTexto(texto, pontuacao, remove_stopwords, remove_acentuacao_flag):

    texto_processado = texto.lower()
    stopwords = nltk.corpus.stopwords.words('portuguese') 
    
    if remove_acentuacao_flag:
        texto_processado = remove_acentuacao(texto_processado)
        
    tokens = []
    for token in nltk.word_tokenize(texto_processado):
        tokens.append(token)
    
    if pontuacao and remove_stopwords:
        tokens = [palavra for palavra in tokens if palavra not in stopwords and palavra not in string.punctuation]
    elif pontuacao:
        tokens = [palavra for palavra in tokens if palavra not in string.punctuation]
    elif remove_stopwords:
        tokens = [palavra for palavra in tokens if palavra not in stopwords]
     
    if remove_stopwords or pontuacao or remove_acentuacao_flag: 
        texto_processado = ' '.join([str(elemento) for elemento in tokens if not elemento.isdigit()])
    else:
        texto_processado = texto
  
    return texto_processado
def main():
   # st.sidebar.title('Menu')

    # Definindo o menu lateral
    pagina_selecionada = st.sidebar.radio('Menu', [  'Sumarização de Frequência'])
 

    # Verificando a página selecionada e chamando a função correspondente
    if pagina_selecionada == 'Sumarização de Frequência':
            st.title('Sumarização de Frequência')

    st.write("Na sumarização por frequência, verificamos a frequência das palavras para identificar quais são as mais frequentes no texto original. Isso é importante porque as palavras mais frequentes tendem a ser as mais relevantes e significativas para o entendimento do conteúdo. Ao identificar e priorizar essas palavras-chave, podemos resumir o texto destacando os pontos principais e ignorando detalhes menos relevantes. Essa abordagem é útil para extrair automaticamente os pontos essenciais de um texto longo, economizando tempo e facilitando a compreensão.")
    Inicio, Sumarizacao = st.tabs(["Inicio", "Sumarizacao"])

    with Inicio:

       
        st.write("""A biblioteca NLTK (Natural Language Toolkit) contém uma lista de stopwords para vários idiomas, 
             incluindo o português. Essas stopwords são usadas para filtrar palavras irrelevantes em textos,
             permitindo que você se concentre nas palavras-chave e significativas em uma análise de texto.""")
        stopwords = nltk.corpus.stopwords.words('portuguese')
        # Converter a lista de stopwords em um DataFrame do pandas
        df_stopwords = pd.DataFrame(stopwords, columns=["Stopwords"])
        # Criar um expander para a tabela de stopwords
        with st.expander("Ver Stopwords"):
            # Exibir a tabela de stopwords com rolagem dentro do expander
            st.write("Aqui estão as stopwords em português:")
            st.table(df_stopwords)  
            st.write("Para remover a pontuação estaremos utilizando a constante punctuation modulo string do python, que contém todos os caracteres de pontuação definidos no conjunto de caracteres ASCII ")    
            st.write(f"Lista pontuações a que serão removidas:  {string.punctuation}")
            
            st.write("A remoção de acentuação está sendo realizada utilizando o unicodedata do python.") 
            st.write("Os acentos removidos incluem: Agudo (´), Circunflexo (^), Grave (`), Tilde (~), Trema (¨) e Cedilha (¸).")
            texto_exemplo_inicio ="""Processamento de língua natural (PLN) é uma subárea da ciência da computação, inteligência artificial e da linguística que estuda os problemas da geração e compreensão automática de línguas humanas naturais. Sistemas de geração de língua natural convertem informação de bancos de dados de computadores em linguagem compreensível ao ser humano e sistemas de compreensão de língua natural convertem ocorrências de linguagem humana em representações mais formais, mais facilmente manipuláveis por programas de computador. Alguns desafios do PLN são compreensão de língua natural, fazer com que computadores extraiam sentido de linguagem humana ou natural e geração de língua natural"""
            st.divider()             
       
        # Adicionando um campo de entrada de texto (text area)
        texto_original_inicio = st.text_area("Insira o texto aqui:", texto_exemplo_inicio, height=200)
        col1, col2, col3 = st.columns(3)  
        with col1:
            remove_pontuacao_flag = st.toggle('Remove pontuacao')
        with col2:
            remove_stopwords_flag = st.toggle('Remove stopwords')
        with col3:
            remove_acentuacao_flag = st.toggle('Remove acentuacao')
        # Adicionando um botão para capturar o texto e exibi-lo
        if st.button('Enviar'):
           texto_processado = processaTexto(texto_original_inicio, remove_pontuacao_flag, remove_stopwords_flag, remove_acentuacao_flag)
           frequencia_palavras = nltk.FreqDist(nltk.word_tokenize(texto_processado))
           fre_palavras = frequencia_palavras
           peso_palavras = frequencia_palavras
           frequencia_maxima = max(peso_palavras.values())
          
           
           st.write('Texto Processado:')
           st.write(texto_processado)
           st.divider()  
           st.write(f"Frequência maxíma (Número de vezes que a mesma palavra ocorre no documento): {frequencia_maxima}")
           st.divider() 
           st.subheader('Frequência das palavras')
           st.write('Frequência das palavras: As palavras que aparecem com mais frequência no texto original geralmente são aquelas que carregam mais significado e relevância. Portanto, ao analisar a frequência das palavras, podemos identificar quais são os termos mais importantes para incluir na sumarização.')
           st.write(fre_palavras)
           st.divider() 
           for palavra in peso_palavras.keys():
               peso_palavras[palavra] = (peso_palavras[palavra] / frequencia_maxima)
           st.subheader('Pesos das palavras')
           markdown_content = """
            Além da frequência das palavras, também consideramos o peso delas com base no TF-IDF.
            Esse método leva em conta não apenas a frequência de uma palavra em um texto, mas também a frequência dela em relação a outros documentos. 
            Isso é útil porque algumas palavras podem ser comuns em geral, mas têm menos peso se aparecerem em muitos documentos.
            Por outro lado, palavras menos comuns em geral, mas que aparecem frequentemente em um texto específico, podem ter um peso maior.'         
           
            A fórmula TF-IDF (Term Frequency-Inverse Document Frequency) é uma medida estatística utilizada para avaliar a importância de uma palavra em um documento em relação a um corpus. 
            
            Ela é calculada da seguinte forma: peso = frequência da palavra / frequência máxima
           
            """
           st.markdown(markdown_content)
           st.write(peso_palavras)
           lista_sentencas = nltk.sent_tokenize(texto_original_inicio)
           
           
           st.write("Verificando a pontução de cada frase")
           #verificando qual das são as frases mais relevantes considerando a soma das palavras
           nota_sentencas = {}
           for sentenca in lista_sentencas:
             for palavra in nltk.word_tokenize(sentenca.lower()):
                #print(palavra)
                if palavra in frequencia_palavras.keys():
                    if sentenca not in nota_sentencas.keys():
                        nota_sentencas[sentenca] = frequencia_palavras[palavra]
                    else:
                        nota_sentencas[sentenca] += frequencia_palavras[palavra] 
           st.write(nota_sentencas)
           #Definiando a quantidade de frases que será utuilizada no resumo neste caso irá reduzir aproximadamente 50% do texto
           percetualTexto =  len(lista_sentencas)/2
           percetualTexto = math.ceil(percetualTexto)
           melhores_sentencas = heapq.nlargest(percetualTexto, nota_sentencas, key=nota_sentencas.get)
           resumo = ' '.join(melhores_sentencas)
           st.write(f"Resumo final")
           st.write(resumo)
           
 

if __name__ == "__main__":
    main()

