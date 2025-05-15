import cv2

def escala_cinza(img): # converte a imagem de RGB para grayscale
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

def inverter_cores(img): # inverte as cores da imagem
    return cv2.bitwise_not(img) 

def desfoque(img, k=21): # aplica um desfoque na imagem
    return cv2.blur(img, (k, k)) 

def aumentar_contraste(img): # aumenta o contraste da imagem usando CLAHE
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # parâmetros padrão
    l_clahe = clahe.apply(l)
    lab_clahe = cv2.merge((l_clahe, a, b))
    return cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)

def rotacionar(img, angulo=90):
    h, w = img.shape[:2]
    centro = (w // 2, h // 2)
    matriz = cv2.getRotationMatrix2D(centro, angulo, 1.0)
    return cv2.warpAffine(img, matriz, (w, h))

def redimensionar(img, nova_largura=300, nova_altura=300):
    try:
        return cv2.resize(img, (nova_largura, nova_altura), interpolation=cv2.INTER_AREA)
    except:
        return img  # se der erro, retorna original