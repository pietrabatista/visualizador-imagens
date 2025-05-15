import FreeSimpleGUI as sg # biblioteca que facilita a construção de uma interface visual simples e que o usuário consegue interagir 
import cv2 # biblioteca opencv de processamento de imagens
import filtros # módulo onde estão todos os meus filtros criados para essa atividade 
from interface import tela, cv2_to_bytes

def main():
    window = tela()
    original = None
    modificada = None

    while True: # loop infinito para manter a janela aberta e processar os eventos (tornando responsiva)
        event, values = window.read() # lê os eventos da janela, ou seja, o que o usuário está fazendo na interface. O evento é o que o usuário fez (clicou em um botão, por exemplo) e os values são os valores dos inputs da interface (se houver algum).
        if event in (sg.WIN_CLOSED, "EXIT"): # verifica se o usuário fechou a janela ou clicou no botão de sair
            break

        if event == "Upload": # verifica se o botão Upload foi clicado
            path = sg.popup_get_file("Escolha uma imagem", file_types=(("ALL Files", "*.png;*.jpg;*.jpeg"),)) # função do simpleGUI Display que abre um janela popup com um texto de entrada e um butão de browse para permitir que o usuário escolha o seu arquivo.
            if path:
                original = cv2.imread(path) #lê a imagem escolhida usando o OpenCV
                modificada = original.copy() #cópia da imagem original. a ideia aqui é preservar a original e aplicar os filtros apenas na modificada.
                window["-ORIGINAL-"].update(data=cv2_to_bytes(original)) # mostra a imagem original na interface e converte a imagem para um formato que o PySimpleGUI consegue mostrar na tela
                window["-MODIFICADA-"].update(data=cv2_to_bytes(modificada)) # mostra a imagem modificada na interface, no outro painel da janela.

        elif event == "Cinza":
            if modificada is None:
                sg.popup_error("Nenhuma imagem carregada", "Por favor, carregue uma imagem antes de aplicar filtros.")
            else:
                modificada = filtros.escala_cinza(modificada)
                modificada = cv2.cvtColor(modificada, cv2.COLOR_GRAY2BGR)
                window["-MODIFICADA-"].update(data=cv2_to_bytes(modificada))

        elif event == "Reset" and original is not None:
            modificada = original.copy()
            window["-MODIFICADA-"].update(data=cv2_to_bytes(modificada))

        elif event == "Inverter":
            if modificada is None:
                sg.popup_error("Nenhuma imagem carregada", "Por favor, carregue uma imagem antes de aplicar filtros.")
            else:
                modificada = filtros.inverter_cores(modificada)
                window["-MODIFICADA-"].update(data=cv2_to_bytes(modificada))

        elif event == "Blur":
            if modificada is None:
                sg.popup_error("Nenhuma imagem carregada", "Por favor, carregue uma imagem antes de aplicar filtros.")
            else:
                modificada = filtros.desfoque(modificada)
                window["-MODIFICADA-"].update(data=cv2_to_bytes(modificada))

        elif event == "Contraste":
            if modificada is None:
                sg.popup_error("Nenhuma imagem carregada", "Por favor, carregue uma imagem antes de aplicar filtros.")
            else:
                modificada = filtros.aumentar_contraste(modificada)
                window["-MODIFICADA-"].update(data=cv2_to_bytes(modificada))

        elif event == "Rotacionar":
            if modificada is None:
                sg.popup_error("Carregue uma imagem primeiro.")
            else:
                modificada = filtros.rotacionar(modificada)
                window["-MODIFICADA-"].update(data=cv2_to_bytes(modificada))

        elif event == "Redimensionar":
            if modificada is None:
                sg.popup_error("Carregue uma imagem primeiro.")
            else:
                nova_largura = sg.popup_get_text("Nova largura (px):", default_text="300")
                nova_altura = sg.popup_get_text("Nova altura (px):", default_text="300")

                try:
                    nova_largura = int(nova_largura)
                    nova_altura = int(nova_altura)

                    if nova_largura <= 0 or nova_altura <= 0:
                        raise ValueError("Largura e altura devem ser maiores que zero.")
                    
                    modificada = filtros.redimensionar(modificada, nova_largura, nova_altura)
                    window["-MODIFICADA-"].update(data=cv2_to_bytes(modificada))
                except:
                    sg.popup_error("Digite valores válidos.")

        elif event == "Salvar":
            if modificada is None:
                sg.popup_error("Nada para salvar", "Carregue e modifique uma imagem antes de salvar.")
            else:
                save_path = sg.popup_get_file("Salvar imagem como...", save_as=True, file_types=(("PNG", "*.png"),))
            if save_path:
                cv2.imwrite(save_path, modificada)

    window.close()

if __name__ == "__main__":
    main()
