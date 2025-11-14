# PERGUNTAR PRA HERMAN PRA QUE ISSO SERVE E PRA QUE USAR

import numpy as np
import cv2 as cv

def ahe(img, janela):
    linha, coluna = img.shape
    meio_janela = janela // 2
    saida = np.zeros(img.shape)

    for i in range(linha):
        for j in range(coluna):
                y1 = max(0, i - meio_janela)
                y2 = min(linha, i + meio_janela + 1)

                x1 = max(0, j - meio_janela)
                x2 = min(coluna, j + meio_janela + 1)

                regiao = img[y1:y2, x1:x2]
                
                # Equalizando o Histograma da imagem
                histograma = cv.calcHist([regiao], [0], None, [256], [0, 256])
                cdf = histograma.cumsum()
                histograma_normalizado = cdf / cdf[-1] # Isso aqui normaliza

                ################################################################################################
                # Com OpenCV
                #histograma_normalizado = cv.equalizeHist(regiao)
                #saida[i, j] = histograma_normalizado[i - y1, j - x1]
                ################################################################################################
                
                saida[i, j] = int(255 * histograma_normalizado[img[i, j]])

    return (saida * (-1)).astype(np.uint8)


img = cv.imread("imagens_usadas_para_testes/Imagem_clara_e_escura.jpeg", 0)
img = cv.resize(img, (800, 600))

img_saida = ahe(img, 15)
cv.imshow("saida", img_saida)
cv.waitKey(0)
cv.destroyAllWindows()

################################################################################################################
# Com OpenCV
# Não fazem exatamente a mesma coisa
img = cv.imread("imagens_usadas_para_testes/pouco_contraste.jpg", 0)
img = cv.resize(img, (800, 600))

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_saida = clahe.apply(img)

cv.imshow("Original", img)
cv.imshow("resultado", img_saida)
cv.waitKey(0)
cv.destroyAllWindows()
