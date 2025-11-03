# Forma geral de transformação logaritmica
# s = c log (1 + r)
# c é uma constante
# r >= 0
# para expandir os valores de pixels mais escuros em uma imagem ao mesmo tempo em que comprimimos os valores de nível mais alto. O oposto
# se aplica à transformação logarítmica inversa

import cv2 as cv
import numpy as np

img = cv.imread("OpenCV/Livro/SP-Alto-Contraste.jpg")
img_cp = img.astype(np.float32)
img_cp = (255/np.log(256)) * np.log(img + 1)
img_cp = np.uint8(img_cp)

cv.imshow("IMG", img_cp)
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()