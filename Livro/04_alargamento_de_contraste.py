import cv2 as cv
import numpy as np

def corrige_tamanho(img):
    return cv.resize(img, (800, 600))

img = cv.imread("imagens_usadas_para_testes/pouco_contraste.jpg")
img = corrige_tamanho(img)
img_cp = img.astype(np.float32)
r_min, r_max = np.min(img_cp), np.max(img_cp)

img_saida = ((img_cp - r_min) / (r_max - r_min))* 255
img_saida = img_saida.astype(np.uint8)

cv.imshow("Original", img)
cv.imshow("Saida", img_saida)
cv.waitKey(0)
cv.destroyAllWindows()