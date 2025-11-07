import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("imagens_usadas_para_testes/magem_muito_colorida.jpg")
img = cv.resize(img, (800, 600))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

hist = [0] * 256
for linha in img:
    for pixel in linha:
        hist[int(pixel)] += 1

# gráfico
plt.bar(range(256), hist, width=0.8)
plt.title("Histograma")
plt.xlabel("Nível de intensidade")
plt.ylabel("Frequência")
plt.show()

################################################################################################################

# com OpenCV

img = cv.imread("imagens_usadas_para_testes/magem_muito_colorida.jpg")
img = cv.resize(img, (800, 600))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

hist = cv.calcHist([img], [0], None, [256], [0, 256]) # ([imagem], [canal usado - 0 = gray], [Máscara aplicada], [Número de bins], [faixa de intensidade])
hist = hist.flatten()                                 # achata o array para 1D

# gráfico
plt.bar(range(256), hist, width=0.8)
plt.title("Histograma (OpenCV)")
plt.xlabel("Nível de intensidade")
plt.ylabel("Frequência")
plt.show()