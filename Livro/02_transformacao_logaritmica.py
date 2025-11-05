# Forma geral de transformação logaritmica
# s = c log (1 + r)
# c é uma constante
# r >= 0 # r é a imagem de entrada
# para expandir os valores de pixels mais escuros em uma imagem ao mesmo tempo em que comprimimos os valores de nível mais alto. O oposto
# se aplica à transformação logarítmica inversa

import cv2 as cv
import numpy as np

img_cidade_sp = cv.imread("imagens_usadas_para_testes/SP-Alto-Contraste.jpg")

# Apos alguns experimentos, descobri que melhor não somar esse 1 na fórmula abaixo
#img_cidade_sp_cp = c * log(img_cidade_sp + 1)

#img_cidade_sp_cp = (255/np.log(256)) * np.log(img_cidade_sp + 1)
#img_cidade_sp_cp = np.uint8(img_cidade_sp_cp)

img_cidade_sp_cp_sem_1 = img_cidade_sp.astype(np.float32)
img_cidade_sp_cp_sem_1 = (255/np.log(256)) * np.log(img_cidade_sp_cp_sem_1)
img_cidade_sp_cp_sem_1 = np.uint8(img_cidade_sp_cp_sem_1)

#cv.imshow("Imagem_Original", img_cidade_sp_cp)
cv.imshow("Imagem logaritmica", img_cidade_sp_cp_sem_1)
cv.imshow("Original", img_cidade_sp)

cv.waitKey(0)
cv.destroyAllWindows()

################################################################################################################

# Experimento - e se eu pegar uma imagem colorida e escurecer ela?
img_colorida = cv.imread("imagens_usadas_para_testes/magem_muito_colorida.jpg")
largura = 800
altura = 600
img_colorida_red = cv.resize(img_colorida, (largura, altura))
img_colorida = cv.resize(img_colorida, (largura, altura))

img_colorida_escura = cv.convertScaleAbs(img_colorida, alpha=0.2, beta=0)
img_colorida_escura = cv.resize(img_colorida_escura, (largura, altura))

img_colorida_float = img_colorida_escura.astype(np.float32)
c = 255 / np.log(1 + np.max(img_colorida_float))
img_colorida_clara = c * np.log(img_colorida_float)

cv.imshow("Original", img_colorida)
cv.imshow("Clareada", img_colorida_clara)
cv.imshow("Escurecida", img_colorida_escura)
cv.waitKey(0)
cv.destroyAllWindows()

# Não funcionou muito bem.


# Experimento - imagem escura de um parque
img_parque_escuro = cv.imread("imagens_usadas_para_testes/imagemescuradoparque.jpeg")
img_parque_escuro_red = cv.resize(img_parque_escuro, (largura, altura))

img_parque_escuro_float = img_parque_escuro_red.astype(np.float32)
c = 255 / np.log(1 + np.max(img_parque_escuro_float))
img_parque_escuro_clareada = c * np.log(img_parque_escuro_float+1)

img_parque_escuro_clareada = np.clip(img_parque_escuro_clareada, 0, 255)  # Garante que fique no intervalo [0,255]
img_parque_escuro_clareada = np.uint8(img_parque_escuro_clareada)         # Converte para 8 bits (valores de 0 a 255)

cv.imshow("Original", img_parque_escuro_red)
cv.imshow("Clareada", img_parque_escuro_clareada)                      # imshow espera uma imagem 8 bits
cv.waitKey(0)
cv.destroyAllWindows()

# Esse deu muito certo

################################################################################################################

# com OpenCV

def transformar_logaritmica(img):
    # Converte para float e evita log(0)
    img_float = img.astype(np.float32) + 1.0               # Aplica logaritmo natural com OpenCV
    img_log = cv.log(img_float)                            # Normaliza para o intervalo 0–255
    cv.normalize(img_log, img_log, 0, 255, cv.NORM_MINMAX) # Converte de volta para 8 bits
    img_log = cv.resize(img_log, (800, 600))

    return np.uint8(img_log)

log_cidade_sp = transformar_logaritmica(img_cidade_sp)
log_colorida = transformar_logaritmica(img_colorida)
log_parque_escuro = transformar_logaritmica(img_parque_escuro)

# --- Exibe todas ---
cv.imshow("Cidade SP - Logaritmica", log_cidade_sp)
cv.imshow("Imagem Colorida - Logaritmica", log_colorida)
cv.imshow("Parque Escuro - Logaritmica", log_parque_escuro)

cv.waitKey(0)
cv.destroyAllWindows()