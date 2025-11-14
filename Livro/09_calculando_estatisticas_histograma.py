import cv2 as cv
import numpy as np

def var(img):
    mean = np.mean(img)
    soma = 0
    for l in img:
        for p in l:
            soma += (p - mean)**2
    
    return (soma / (img.shape[0] * img.shape[1]))

# Lendo img
img = cv.imread("imagens_usadas_para_testes/pouco_contraste.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.resize(img, (800, 600))

# Hist
hist = cv.calcHist([img], [0], None, [256], [0, 256])

mean = np.mean(hist).astype(int)
variancia  = np.var(hist)