 # Atividade Visualizador de Imagens

Essa atividade foi desenvolvida com o objetivo de criar um **visualizador de imagens interativo**, que permite aplicar filtros e transformações através de uma interface gráfica. Para assisir o vídeo de demonstração clique [aqui](https://drive.google.com/file/d/18303PHA5q1-N7aY_BxIGTm6WPgMV-ILa/view?usp=sharing)

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

## Referências

- https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html
- https://docs.opencv.org/4.x/d7/da8/tutorial_table_of_content_imgproc.html
- https://www.geeksforgeeks.org/python-grayscaling-of-images-using-opencv/
- https://freesimplegui.readthedocs.io/en/latest/call%20reference/
- https://docs.pysimplegui.com/en/latest/cookbook/ecookbook/
- https://www.youtube.com/watch?v=TBG7c9Ep3pE
- https://stackoverflow.com/questions/17967320/python-opencv-convert-image-to-byte-string
- https://www.geeksforgeeks.org/image-enhancement-techniques-using-opencv-python/