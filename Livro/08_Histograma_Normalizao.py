import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread("imagens_usadas_para_testes/pouco_contraste.jpg")
img = cv.resize(img, (800, 600))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Primeiro passo: Calcular o Histograma
histograma = cv.calcHist([img], [0], None, [256], [0, 256]).flatten()
pdf = histograma / histograma.sum()
cdf = np.cumsum(pdf)

# CDF e normalização
hist_normalizado = (255 * cdf).round().astype(np.uint8)

# gráfico
plt.bar(range(256), hist_normalizado, width=0.8)
plt.title("Histograma Normalizado")
plt.xlabel("Nível de intensidade")
plt.ylabel("Frequência")
plt.show()

################################################################################################################

# Com OpenCV
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()