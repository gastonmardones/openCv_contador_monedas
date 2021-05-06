import cv2 as cv
import numpy as np
valorGauss = 5   # Variables, modificables a gusto para ver cual queda mejor
valorKernel = 7
def buscarMonedas(n_img):
    original = cv.imread(f'monedas-{n_img}.jpg')
    gris = cv.cvtColor(original, cv.COLOR_BGR2GRAY) # pasa la imagen original a escala de grises elegida
    gauss = cv.GaussianBlur(gris, (valorGauss, valorGauss), cv.BORDER_DEFAULT)         # reducción de ruido de la imagen
    canny = cv.Canny(gauss, 10, 100)        # Solo los bordes
    dilated = cv.dilate(canny, (5,5), iterations=3)
    kernel = np.ones((valorKernel,valorKernel), np.uint8)
    cierre = cv.morphologyEx(dilated, cv.MORPH_CLOSE, kernel)
    # cv.imshow('Original', original)
    # cv.imshow('Resultado', resize)
    # cv.imshow('Grises', gris)
    # cv.imshow('Gauss', gauss)
    # cv.imshow('Canny', canny)
    # cv.imshow('Dilated', dilated)
    # cv.imshow('Cierre', cierre)
    

    cv.waitKey(0)
    cv.destroyAllWindows()
    
for i in range(12):
    buscarMonedas(i+1)
    
