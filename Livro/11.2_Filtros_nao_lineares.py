import cv2 as cv
import numpy as np

def filtro_mediana(imagem, tamanho_mask):
    altura = len(imagem)
    largura = len(imagem[0])
    
    k = tamanho_mask // 2
    resultado = [[0 for _ in range(largura)] for _ in range(altura)]

    for y in range(altura):
        for x in range(largura):

            vizinhos = []

            # percorre a vizinhança
            for dy in range(-k, k + 1):
                for dx in range(-k, k + 1):

                    ny = y + dy
                    nx = x + dx

                    # borda
                    if 0 <= ny < altura and 0 <= nx < largura:
                        vizinhos.append(imagem[ny][nx])

            # ordena e pega a mediana
            vizinhos.sort()
            meio = len(vizinhos) // 2
            resultado[y][x] = vizinhos[meio]

    return resultado


img = cv.imread("imagens_usadas_para_testes/pouco_contraste.jpg", 0)
img = cv.resize(img, (800, 600))

saida = img.astype(np.float32)
saida = filtro_mediana(saida, 5)
saida = np.array(saida, dtype=np.uint8)

cv.imshow("Original", img)
cv.imshow("Transformada", saida)
cv.waitKey(0)
cv.destroyAllWindows()