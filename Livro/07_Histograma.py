import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("imagens_usadas_para_testes/magem_muito_colorida.jpg")
img = cv.resize(img, (800, 600))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_cp = img.copy()
img = img.astype(np.float32)

hist = [0] * 256
for linha in img:
    for pixel in linha:
        hist[int(pixel)] += 1

img = img.astype(np.uint8)

# gráfico
plt.bar(range(256), hist, width=0.8)
plt.title("Histograma")
plt.xlabel("Nível de intensidade")
plt.ylabel("Frequência")
plt.show()