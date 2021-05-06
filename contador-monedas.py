import cv2 as cv
import numpy as np
def buscarMonedas(n_img):
    original = cv.imread(f'monedas-{n_img}.jpg')
    cv.waitKey(0)
    cv.destroyAllWindows()
for i in range(12):
    buscarMonedas(i+1)
