import cv2 as cv
import numpy as np


valorGauss = 5   # Variables, modificables a gusto para ver cual queda mejor
valorKernel = 7

def rescaleFrame(frame, scale=0.5):         # Funcion para reescalar el frame, funciona para img,videos and live
    width = int(frame.shape[1] * scale)     # shape[1] es el width
    height = int(frame.shape[0] * scale)    # shape[0] es el height
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    

def buscarMonedas(n_img):
    original = cv.imread(f'monedas-{n_img}.jpg')
    # resize = rescaleFrame(original)
    gris = cv.cvtColor(original, cv.COLOR_BGR2GRAY) # pasa la imagen original a escala de grises elegida
    gauss = cv.GaussianBlur(gris, (valorGauss, valorGauss), cv.BORDER_DEFAULT)         # reducción de ruido de la imagen
    canny = cv.Canny(gauss, 10, 100)        # Solo los bordes
    dilated = cv.dilate(canny, (5,5), iterations=3)
    kernel = np.ones((valorKernel,valorKernel), np.uint8)
    cierre = cv.morphologyEx(dilated, cv.MORPH_CLOSE, kernel)
    

    contornos, jerarquia = cv.findContours(cierre, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    print(f'monedas encontradas:{len(contornos)}')
    cv.drawContours(original, contornos, -1, (0,0,255), 2)
    cv.putText(original, f'Contornos encontrados: {len(contornos)}', (50,50), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0),2)

    # cv.imshow('Original', original)
    # cv.imshow('Resultado', resize)
    # cv.imshow('Grises', gris)
    # cv.imshow('Gauss', gauss)
    # cv.imshow('Canny', canny)
    # cv.imshow('Dilated', dilated)
    # cv.imshow('Cierre', cierre)
    cv.imshow('Resultado', original)
    

    cv.waitKey(0)
    cv.destroyAllWindows()
    
for i in range(12):
    buscarMonedas(i+1)
    
