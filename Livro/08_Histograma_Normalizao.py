import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread("imagens_usadas_para_testes/magem_muito_colorida.jpg")
img = cv.resize(img, (800, 600))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Primeiro passo: Calcular o Histograma
histograma = cv.calcHist([img], [0], None, [256], [0, 256])
histograma = histograma.flatten()

# Normaliza o Histograma para depois aplicar na imagem
histograma_normalizado = histograma / (img.shape[0] * img.shape[1])

