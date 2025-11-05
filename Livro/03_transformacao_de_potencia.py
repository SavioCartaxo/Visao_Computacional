"""
# Teoria
# Transformação de potencia usada para ## Transformação gamma ##
# Aumenta o contraste.

Usado para corrigir como a tela exibe a luminosidade ou para realçar detalhes em áreas escuras ou claras.
Ajustar o brilho e o contraste de uma imagem de forma não linear

A transformação de potência (ou correção gama) é dada por:
s = c * r**y

r = imagen de entreada
s = imagem de saida

y = expoente de correcao
    Normalmente calculado com: 
    mean = np.mean(cv.cvtColor(img, cv.COLOR_BGR2GRAY))
    y = media distribuida em 2 limiares
    
    y < 1 -> clareia imagem
    y = 1 -> sem alteração
    y > 1 -> escurece a imagem

c = coonstante de escala(geralmente 1)
    Normalmente calculado com:
    c = 255/ (255 ** y)

    c = 1   Normal
    c > 1	Mais clara	Amplifica os tons, aumentando brilho geral
    c < 1	Mais escura	Reduz intensidade, diminuindo brilho global

# Dica extra - Aplicar correção gama adaptativa dependendo do histograma (variaçaõ de y)

"""
################################################################################################################
import cv2 as cv
import numpy as np

img = cv.imread("imagens_usadas_para_testes/imagemescuradoparque.jpeg")
img = cv.resize(img, (800, 600))

# essa foi a dica extra
media = np.mean(cv.cvtColor(img, cv.COLOR_BGR2GRAY))
y = 1.5 if media > 128 else 0.7
c = 255 / (255 ** y)

# Tratando a imagem
img_32 = img.astype(np.float32)
img_tratada = c * (img_32 ** y)
img_tratada = np.uint8(img_tratada)   # Essa parte eu sempre esqueço -> np.uint8(img)

cv.imshow("Imagem Original", img)
cv.imshow("Imagem Tratada", img_tratada)
cv.waitKey(0)
cv.destroyAllWindows()

################################################################################################################

"""
obs.:
a formula tambem pode ser representada por:
s = c * ((r + e) ** y)

onde "e" é uma constante de compensação (offset), 
"e" serve para evitar que valores muito baixos de intensidade (quase zero)

0.01 <= e <= 1    Levanta levemente as sombras
e > 5             Clareia bastante a imagem base

"""

################################################################################################################

# E com OpenCV?
# não tem função que faça isso, oq é uma pena, pois o resultado do clareamento ficou muito bom