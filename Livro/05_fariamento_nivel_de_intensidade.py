"""
# Teoria

Definir uma metrica para que apenas um pedaço do aspectro seja destacado

"""

import cv2 as cv
import numpy as np

def corrige_tamanho(img):
    return cv.resize(img, (800, 600))

img = cv.imread("imagens_usadas_para_testes/pouco_contraste.jpg")
img = corrige_tamanho(img)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Definindo a mascara
img_saida = img.astype(np.float32)

mask = (img >= 0) & (img <= 60)
not_mask = (img > 60)

img_saida[mask] = 0
img_saida[not_mask] = 120

img_saida = img_saida.astype(np.uint8)

cv.imshow("Original", img)
cv.imshow("Saida", img_saida)
cv.waitKey(0)
cv.destroyAllWindows()