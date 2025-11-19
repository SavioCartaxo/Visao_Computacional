import cv2 as cv
import numpy as np

def filtro_media(imagem, tamanho_mask):
    altura = len(imagem)
    largura = len(imagem[0])
    
    k = tamanho_mask // 2
    resultado = [[0 for _ in range(largura)] for _ in range(altura)]

    for y in range(altura):
        for x in range(largura):

            soma = 0
            cont = 0  # <-- CORREÇÃO: reseta a cada pixel

            for d_y in range(-k, k + 1):
                for d_x in range(-k, k + 1):

                    ny = y + d_y
                    nx = x + d_x

                    if 0 <= ny < altura and 0 <= nx < largura:
                        soma += imagem[ny][nx]
                        cont += 1

            resultado[y][x] = soma / cont

    return resultado

img = cv.imread("imagens_usadas_para_testes/pouco_contraste.jpg", 0)
img = cv.resize(img, (800, 600))

saida = img.astype(np.float32)
saida = filtro_media(saida, 3)
saida = np.array(saida, dtype=np.uint8)

cv.imshow("Original", img)
cv.imshow("Transformada", saida)
cv.waitKey(0)
cv.destroyAllWindows()