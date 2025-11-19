import numpy as np

def correlacao(imagem, mascara):
    imagem  = np.asarray(imagem, dtype=float)
    mascara = np.asarray(mascara, dtype=float)

    altura_img, largura_img = imagem.shape
    altura_mask, largura_mask = mascara.shape

    pad_y = altura_mask // 2
    pad_x = largura_mask // 2

    # adiciona borda de zeros
    imagem_padded = np.pad(
        imagem,
        ((pad_y, pad_y), (pad_x, pad_x)),
        mode="constant",
        constant_values=0.0
    )

    # matriz de saída
    resultado = np.zeros_like(imagem, dtype=float)

    # aplica correlação
    for y in range(altura_img):
        for x in range(largura_img):
            
            soma = 0.0
            for i in range(altura_mask):
                for j in range(largura_mask):

                    pixel = imagem_padded[y + i, x + j]
                    peso  = mascara[i, j]
                    soma += pixel * peso

            resultado[y, x] = soma

    return resultado

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mask = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

print(correlacao(matriz, mask))

################################################################################################################
#Com OpenCV

import cv2 as cv

imagem = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
], dtype=np.float32)

mascara = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
], dtype=np.float32)

resultado = cv.filter2D(
    imagem,
    ddepth=-1,
    kernel=mascara,
    borderType=cv.BORDER_CONSTANT
)

print(resultado)