 # Atividade Visualizador de Imagens

Essa atividade foi desenvolvida com o objetivo de criar um **visualizador de imagens interativo**, que permite aplicar filtros e transformações através de uma interface gráfica.

## Funcionalidades

- Carregamento de imagem via explorador de arquivos
- Exibição lado a lado da imagem original e modificada
- Filtros aplicáveis:
  - Escala de Cinza
  - Inversão de Cores
  - Desfoque (Blur)
  - Aumento de Contraste
- Transformações:
  - Rotação da imagem (90° por clique)
  - Redimensionamento (definido pelo usuário)
- Salvar imagem resultante
- Resetar para imagem original

## Tecnologias utilizadas

- Python 3.12
- OpenCV
- FreeSimpleGUI 

## Como executar o projeto

1. Clone este repositório
2. Crie e ative um ambiente virtual:

    - python -m venv venv

   -  .\venv\Scripts\activate   # Windows

3. Instale as dependências:

   -  pip install -r requirements.txt

4. Execute o programa:

   -  python main.py
