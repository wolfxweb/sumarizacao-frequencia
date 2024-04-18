# Projeto Sumarização de Texto com Frequência de Palavras

## Descrição
Este projeto visa implementar uma técnica de sumarização de texto baseada na frequência das palavras. A sumarização de texto é uma técnica importante em processamento de linguagem natural (PLN) que permite extrair as informações mais relevantes de um texto de entrada de maneira concisa. Neste projeto, utilizamos a abordagem de frequência de palavras, que consiste em identificar as palavras mais frequentes no texto e usá-las para criar um resumo.

## Funcionamento
1. **Pré-processamento de Texto:**
   O texto de entrada passa por um processo de pré-processamento para remover pontuação, stopwords e normalizar o texto.

2. **Cálculo da Frequência das Palavras:**
   Em seguida, calculamos a frequência de cada palavra no texto, atribuindo pesos às palavras com base em sua ocorrência.

3. **Seleção das Palavras Chave:**
   As palavras mais frequentes são selecionadas como palavras-chave para o resumo. Isso é feito utilizando técnicas de ordenação ou definindo um limite de frequência.

4. **Geração do Resumo:**
   Por fim, o resumo é gerado selecionando as frases que contêm as palavras-chave mais relevantes, ou combinando as palavras-chave em uma nova frase.

## Uso do Streamlit
Este projeto utiliza o Streamlit para criar uma interface web interativa onde os usuários podem inserir um texto de entrada e visualizar o resumo gerado pela técnica de sumarização de texto com frequência de palavras.

## Instalação e Execução
1. **Clone o Repositório:**

2. **Crie um Ambiente Virtual:**
    cd seu_projeto
    python -m venv venv

3. **Ative o Ambiente Virtual:**
- No Windows:
  ```
  venv\Scripts\activate
  ```
- No Linux/Mac:
  ```
  source venv/bin/activate
  ```

4. **Instale as Dependências:**
pip install -r requirements.txt


5. **Execute o Streamlit:**
streamlit run app.py



6. **Acesse a Aplicação:**
Acesse a aplicação no navegador usando o link fornecido pelo Streamlit, geralmente é algo como `http://localhost:8501`.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request.







