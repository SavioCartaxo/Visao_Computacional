"""
# Teoria

Imagens de baixo contraste podem ser resultado de iluminação ruim
    
    O alargamento de contraste é um processo que expande a faixa de níveis de intensidade de uma imagem 
    de modo a incluir todo o intervalo de intensidades do meio de gravação ou do dispositivo de exibição.
    
    Utiliza o nivel max e min de intensidade da imagem para diminuir o contraste
    
    Fatiamento de intensidade:
    Pode ser interessante enfatizar um intervalo específico de intensidades em uma imagem. As aplicações 
    incluem o realce de características como massas de água em imagens de satélite e o realce de falhas 
    em imagens de raios X.

    s = (r - r_min) / (r_max - r_min) * (255)

"""

################################################################################################################

import cv2 as cv
import numpy as np

def corrige_tamanho(img):
    return cv.resize(img, (800, 600))

img = cv.imread("imagens_usadas_para_testes/pouco_contraste.jpg")
img = corrige_tamanho(img)
img_cp = img.astype(np.float32)
r_min, r_max = np.min(img_cp), np.max(img_cp)

img_saida = (img_cp - r_min) / (r_max - r_min) * 255
img_saida = img_saida.astype(np.uint8)

cv.imshow("Original", img)
cv.imshow("Saida", img_saida)
cv.waitKey(0)
cv.destroyAllWindows()

################################################################################################################
