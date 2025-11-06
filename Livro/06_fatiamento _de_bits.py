"""
# Teoria

fatiamento por planos de bits (bit-plane slicing)
Técnica muito usada para análise de estrutura digital de imagens e COMPRESSÃO.
O fatiamento consiste em separar cada bit desses 8 em uma imagem independente.
Cada uma dessas imagens mostra a contribuição daquele bit específico para o valor total dos pixels.
os bits 0, 1 e 2 sao os mais importantes

"""

import cv2 as cv
import numpy as np

def corrige_tamanho(img):
    return cv.resize(img, (800, 600))

img = cv.imread("imagens_usadas_para_testes/pouco_contraste.jpg")
img = corrige_tamanho(img)

planos = list()

# Extrai cada plano de bit (0 = menos significativo)
for i in range(8):
    plano = cv.bitwise_and(img, 1 < i)
    plano = np.uint8(plano * 255 / (1 << i))
    planos.append(plano)
    cv.imshow(f"Planjo do Bit {i}", plano)

cv.waitKey(0)
cv.destroyAllWindows()