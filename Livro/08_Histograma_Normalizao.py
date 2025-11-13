import cv2 as cv
import numpy as np

img = cv.imread("imagens_usadas_para_testes/Imagem_do_livro.png")
img = cv.resize(img, (800, 600))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY).astype(np.uint8)

# Plot
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()

################################################################################################################
# Importando o matplotlib aqui embaixo para evitar conflito com OpenCV
import matplotlib.pyplot as plt

# Primeiro passo: Calcular o Histograma
histograma = cv.calcHist([img], [0], None, [256], [0, 256]).flatten()
pdf = histograma / histograma.sum()
cdf = np.cumsum(pdf)

# CDF e normalização
hist_normalizado = (255 * cdf).round().astype(np.uint8)

# gráfico Histograma
plt.figure()
plt.bar(range(256), histograma, width=0.8)
plt.title("Histograma")
plt.xlabel("Nível de intensidade")
plt.ylabel("Frequência")

# gráfico Histograma Normalizado
plt.figure()
plt.bar(range(256), hist_normalizado, width=0.8)
plt.title("Histograma Normalizado")
plt.xlabel("Nível de intensidade")
plt.ylabel("Frequência")

plt.show()

################################################################################################################
# Importando o OpenCV aqui embaixo para evitar conflito com matplot
import cv2 as cv

img_saida = hist_normalizado[img]
img_cv = cv.equalizeHist(img)

cv.imshow("img", img)
cv.imshow("Imagem com Histograma Normalizado", img_saida)
cv.waitKey(0)
cv.destroyAllWindows()

################################################################################################################
# Com OpenCV

img_cv = cv.equalizeHist(img)
cv.imshow("Imagem com Histograma Normalizado com OpenCV", img_cv)
cv.waitKey(0)
cv.destroyAllWindows()