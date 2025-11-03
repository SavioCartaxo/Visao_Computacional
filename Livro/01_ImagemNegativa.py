import cv2 as cv

img = cv.imread("one-piece-manga-1060-capa-colorida-postcover.jpg")    
img_negativada =  - img                                           # Isso é a mesma coisa que fazer (-pixel % 256)
img_do_jeito_certo =  255 - img                                   # Esse "Corrige a base", fazendo (-pixel % 255)

cv.imshow("Original", img)
cv.imshow("-img", img_negativada)
cv.imshow("Janela", img_do_jeito_certo)

cv.waitKey(0)
cv.destroyAllWindows()


# E como é no OpenCV?
img = cv.imread("one-piece-manga-1060-capa-colorida-postcover.jpg")
img_invertida = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("Imagem invertida com OpenCV" , img_invertida)
cv.waitKey(0)
cv.destroyAllWindows()