import FreeSimpleGUI as sg
import cv2

sg.theme('LightBrown5') # um tema para deixar mais bonitinho

def cv2_to_bytes(img, max_size=(400, 400)): # converte a imagem para bytes para mostrar na interface
    h, w = img.shape[:2] # pega a altura e largura da imagem
    scale = min(max_size[0]/w, max_size[1]/h) # calcula o fator de escala para redimensionar a imagem
    new_w, new_h = int(w * scale), int(h * scale) 
    resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA) 
    _, buffer = cv2.imencode('.png', resized) # codifica a imagem em formato PNG
    return buffer.tobytes() 

def tela(): # função que cria a tela
    layout = [ 
        [sg.Text("Antes de iniciar, faça o upload de uma imagem", font=("Helvetica", 12))],
        [sg.Image(key="-ORIGINAL-"), sg.Image(key="-MODIFICADA-")], #split na tela, para mostrar as duas imagens lado a lado
        [sg.Button("Upload", button_color=('white', 'springgreen4')), sg.Button("Rotacionar", button_color=('white', 'black')), sg.Button("Redimensionar", button_color=('white', 'black')), sg.Button("Cinza", button_color=('white', 'black')), sg.Button("Inverter", button_color=('white', 'black')), sg.Button("Blur", button_color=('white', 'black')), sg.Button("Contraste", button_color=('white', 'black')), sg.Button("Salvar", button_color=('white', 'black')), sg.Button("Reset", button_color=('white', 'black')), sg.Button("EXIT", button_color=("white", "firebrick3"))]
    ]
    return sg.Window("Visualizador de Imagens", layout, finalize=True)

