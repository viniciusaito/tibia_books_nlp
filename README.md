# Análise de dados dos livros do tibia

## Técnica

- Captura dos dados

    - Baixar todas as letras

    ![diagrama de como os dados seram extraidos](/imgs/diagrama_scrapper.png)

        - httpx + parsel - Tibia Wiki ([Página de bibliotecas](https://www.tibiawiki.com.br/wiki/Bibliotecas))

    - Persistir

        - CSV

- Organização

    - Dataframe - Polars

- Limpeza / tratamento
  - Dataframe
  - Repo de stopwords
- Olhar os dados!
  - Spacy
  - WordCloud

# Análise: Perguntas

- Quais são as palavras mais usadas?
  
  - Por livro
  
  - Por década
  
  - Em que contexto?

- Análise léxica
  
  - Quantas palavras únicas por livro? (média por livro?)
  
  - Quantas palavras únicas por livro?
  
  - Dispersão (onde a palavra ocorre no livro?)

- Gramatica
  
  - Tag

- Ver
  
  - Nuvem de palavras
  
  - Concord
