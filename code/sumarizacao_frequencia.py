import streamlit as st

def sumarizacao_frequencia():
    st.title('Sumarização de Frequência')
    st.write('Esta é a página de Sumarização de Frequência.')

    texto_original = """A inteligência artificial é a inteligência similar à humana. Definem como o estudo de agente artificial com inteligência.Ciência e engenharia de produzir máquinas com inteligência """
    # Adicionando um campo de entrada de texto (text area)
    texto = st.text_area("Insira o texto aqui:", texto_original)

    # Adicionando um botão para capturar o texto e exibi-lo
    if st.button('Enviar'):
        st.write('Texto capturado:')
        st.write(texto)
 

